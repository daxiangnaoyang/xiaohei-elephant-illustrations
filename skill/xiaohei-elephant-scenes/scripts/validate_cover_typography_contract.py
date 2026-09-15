#!/usr/bin/env python3
"""Validate the executable Cover typography contract.

The validator is intentionally dependency-free so Hermes can run it before a
Cover is sent.  It checks the Skill contract, the font provenance in a receipt,
and forbidden base/overlay artifacts in an article asset directory.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
FONT_DEFAULT = Path(
    "/Users/dx/Hermes-agent/00-Agent-Core/assets/fonts/ZCOOLKuaiLe-Regular.woff2"
)
FORBIDDEN_NAME = re.compile(
    r"(?:^|[-_])(base|overlay|text[-_]?layer|composite|merged)(?:[-_.]|$)",
    re.IGNORECASE,
)
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_receipt(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^([a-z][a-z0-9_]*)\s*:\s*(.*)$", raw_line.strip())
        if match:
            values[match.group(1)] = match.group(2).strip()
    return values


def check_source(root: Path) -> list[str]:
    errors: list[str] = []
    required = {
        "SKILL.md": ("Cover 候选最多尝试 8 版", "视觉 QA 不可用"),
        "agents/openai.yaml": (
            "cover-typography-runtime-contract.md",
            "NEEDS_HUMAN",
        ),
        "references/prompt-template.md": (
            "ONE-PASS INTEGRATED COMPOSITION LOCK",
            "Do NOT create a blank/no-text background",
        ),
        "references/qa-checklist.md": (
            "cover-typography-receipt.md",
            "QA 不可用",
        ),
        "GOTCHAS.md": ("标题覆盖物", "视觉 QA 不可用"),
    }
    for relative, tokens in required.items():
        path = root / relative
        if not path.exists():
            errors.append(f"缺少契约文件：{path}")
            continue
        text = path.read_text(encoding="utf-8")
        for token in tokens:
            if token not in text:
                errors.append(f"{path} 缺少硬门禁：{token}")
    font = FONT_DEFAULT
    if not font.exists():
        errors.append(f"全局品牌字体不存在：{font}")
    return errors


def check_artifact_dir(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.is_dir():
        return [f"封面资产目录不存在：{path}"]
    for candidate in sorted(path.rglob("*")):
        if not candidate.is_file() or candidate.suffix.lower() not in IMAGE_SUFFIXES:
            continue
        if FORBIDDEN_NAME.search(candidate.stem):
            errors.append(
                f"发现禁止的 Cover 中间产物：{candidate.name}；禁止 base/overlay/text-layer/composite/merged 血缘"
            )
    return errors


def resolve_path(value: str, receipt: Path) -> Path:
    candidate = Path(value)
    return candidate if candidate.is_absolute() else receipt.parent / candidate


def check_receipt(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        return [f"缺少 Cover 字体运行回执：{path}"]
    values = parse_receipt(path)
    required = (
        "status",
        "generation_passes",
        "cover_attempts",
        "constraint_priority",
        "retry_state",
        "font_asset",
        "font_sha256",
        "typography_reference",
        "imagegen_inputs",
        "final_path",
        "allowed_text",
        "visual_qa",
        "qa_backend",
        "qa_evidence",
    )
    for key in required:
        if not values.get(key):
            errors.append(f"回执字段为空：{key}")

    if values.get("status") != "PASS":
        errors.append("回执 status 必须为 PASS 才能交付")
    if values.get("visual_qa") != "PASS":
        errors.append("回执 visual_qa 必须为 PASS；不可用/报错只能 BLOCKED")
    if values.get("generation_passes") != "1":
        errors.append("Cover 必须恰好一次 image_gen 成型")

    try:
        attempts = int(values.get("cover_attempts", "0"))
    except ValueError:
        attempts = 0
        errors.append("回执 cover_attempts 必须是整数")
    if not 1 <= attempts <= 8:
        errors.append("回执 cover_attempts 必须在 1—8 内；达到 8 仍未收敛应停止并请求人工")

    priority = values.get("constraint_priority", "")
    if not priority.startswith("P0") or "P1" not in priority or "P2" not in priority:
        errors.append("回执 constraint_priority 必须明确 P0 > P1 > P2 的裁决顺序")

    retry_state = values.get("retry_state", "")
    if retry_state not in {"INIT", "CONVERGING", "NEEDS_HUMAN", "PASS"}:
        errors.append("回执 retry_state 必须是 INIT、CONVERGING、NEEDS_HUMAN 或 PASS")
    if values.get("status") == "PASS" and retry_state != "PASS":
        errors.append("status 为 PASS 时 retry_state 必须为 PASS")
    if attempts >= 8 and values.get("status") != "PASS" and retry_state != "NEEDS_HUMAN":
        errors.append("第 8 版仍未通过时必须停止并将 retry_state 写为 NEEDS_HUMAN")

    for field in ("imagegen_inputs", "final_path", "typography_reference"):
        value = values.get(field, "")
        if FORBIDDEN_NAME.search(value):
            errors.append(f"回执 {field} 含有禁止的 base/overlay 等血缘：{value}")

    font = resolve_path(values.get("font_asset", ""), path)
    reference = resolve_path(values.get("typography_reference", ""), path)
    final = resolve_path(values.get("final_path", ""), path)
    for label, target in (("font_asset", font), ("typography_reference", reference), ("final_path", final)):
        if not str(target) or not target.exists():
            errors.append(f"回执 {label} 路径不存在：{target}")

    expected_hash = values.get("font_sha256", "").lower()
    if font.exists() and expected_hash:
        actual_hash = sha256(font)
        if expected_hash != actual_hash:
            errors.append(
                f"字体 SHA-256 不匹配：回执 {expected_hash}，实际 {actual_hash}"
            )

    backend = values.get("qa_backend", "").lower()
    if any(marker in backend for marker in ("unavailable", "error", "429", "400", "blocked", "未验证")):
        errors.append("qa_backend 表示不可用/报错，不能把视觉 QA 写成 PASS")
    evidence = values.get("qa_evidence", "")
    if evidence and (evidence.startswith("/") or evidence.startswith(".")):
        if not resolve_path(evidence, path).exists():
            errors.append(f"QA 证据路径不存在：{evidence}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, default=SKILL_ROOT)
    parser.add_argument("--artifact-dir", type=Path)
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()

    errors = check_source(args.source_root)
    if args.artifact_dir:
        errors.extend(check_artifact_dir(args.artifact_dir))
    if args.receipt:
        errors.extend(check_receipt(args.receipt))

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    print("PASS: Cover typography runtime contract")
    return 0


if __name__ == "__main__":
    sys.exit(main())
