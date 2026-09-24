#!/usr/bin/env python3
"""Run the Hermes/Zhipu lightweight visual QA adapter for a body image.

The body-image gate deliberately checks only the three fast visual contracts:
IP shape, character scale, and the visible-text whitelist.  Paragraph meaning
and information density remain a separate shot-record/3-second-read gate.

This is an external Zhipu adapter, not Codex's native GPT visual route. Codex
should use its current GPT-series runtime for visual understanding. The script
has no third-party dependencies. It uses macOS ``sips`` and ``base64`` for
preprocessing and sends one OpenAI-compatible request with ``curl`` to
GLM-4.6V. It never prints an API key.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


DEFAULT_ENDPOINT = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
DEFAULT_MODEL = "glm-4.6v"
DEFAULT_PROVIDER = "zhipu"
KEY_NAMES = (
    "ZAI_API_KEY",
    "GLM_API_KEY",
    "ZAI_API_KEY_1",
    "ZAI_API_KEY_2",
    "ZAI_API_KEY_3",
    "ZAI_API_KEY_4",
    "ZAI_API_KEY_5",
)
CHECK_NAMES = ("ip_lock", "scale", "text_whitelist")
CHECK_VALUES = {"PASS", "FAIL", "UNCLEAR"}
STATUS_VALUES = {"PASS", "FAIL", "BLOCKED"}


def parse_env_file(path: Path) -> dict[str, str]:
    """Read simple KEY=value entries without executing the file."""

    values: dict[str, str] = {}
    if not path.is_file():
        return values
    for raw_line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[7:].lstrip()
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", key):
            continue
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        values[key] = value
    return values


def load_api_key() -> str | None:
    """Resolve a key from the process environment or Hermes' local env file."""

    for name in KEY_NAMES:
        value = os.environ.get(name, "").strip()
        if value:
            return value

    env_values: dict[str, str] = {}
    for path in (Path.home() / ".hermes" / ".env", Path.home() / ".config" / "hermes" / ".env"):
        env_values.update(parse_env_file(path))
    for name in KEY_NAMES:
        value = env_values.get(name, "").strip()
        if value:
            return value
    return None


def run_command(command: list[str], *, timeout: int) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        check=False,
        capture_output=True,
        text=True,
        timeout=timeout,
    )


def safe_error(message: str, limit: int = 300) -> str:
    """Keep tool errors useful without allowing accidental secret output."""

    cleaned = re.sub(r"Bearer\s+\S+", "Bearer [redacted]", message, flags=re.IGNORECASE)
    return " ".join(cleaned.split())[-limit:]


def thumbnail_base64(image: Path, max_edge: int) -> tuple[str | None, str | None]:
    with tempfile.TemporaryDirectory(prefix="xiaohei-qa-") as temp_dir:
        thumbnail = Path(temp_dir) / "thumbnail.png"
        try:
            sips = run_command(
                [
                    "/usr/bin/sips",
                    "-Z",
                    str(max_edge),
                    "-s",
                    "format",
                    "png",
                    str(image),
                    "--out",
                    str(thumbnail),
                ],
                timeout=30,
            )
        except (OSError, subprocess.TimeoutExpired) as exc:
            return None, f"sips failed: {safe_error(str(exc))}"
        if sips.returncode != 0 or not thumbnail.is_file():
            return None, f"sips failed: {safe_error(sips.stderr or sips.stdout)}"

        try:
            encoded = run_command(["/usr/bin/base64", "-i", str(thumbnail)], timeout=30)
            if encoded.returncode != 0:
                encoded = run_command(["/usr/bin/base64", str(thumbnail)], timeout=30)
        except (OSError, subprocess.TimeoutExpired) as exc:
            return None, f"base64 failed: {safe_error(str(exc))}"
        if encoded.returncode != 0:
            return None, f"base64 failed: {safe_error(encoded.stderr or encoded.stdout)}"
        value = re.sub(r"\s+", "", encoded.stdout)
        if not value:
            return None, "base64 returned an empty image"
        return value, None


def allowed_text_values(args: argparse.Namespace) -> list[str]:
    values = [value.strip() for value in args.allowed_text if value.strip()]
    if args.allowed_text_file:
        values.extend(
            line.strip()
            for line in args.allowed_text_file.read_text(
                encoding="utf-8", errors="replace"
            ).splitlines()
            if line.strip()
        )
    return list(dict.fromkeys(values))


def build_payload(
    image_b64: str,
    *,
    model: str,
    allowed_text: list[str],
) -> dict[str, Any]:
    whitelist = json.dumps(allowed_text, ensure_ascii=False)
    prompt = f"""你是小黑象 2.0 标准 16:9 正文图的快速视觉 QA 门。只检查三项，不做 Cover typography contract，也不替代 shot record 的段落语义和信息密度检查。

1. ip_lock：小黑象必须是轻巧、低矮、哑光黑色剪影；短象鼻、小圆耳、白点眼、身体下方四条短圆桩腿清楚可读。二足、人形腿、火柴腿、鞋脚、膝盖、胖重玩具或写实大象均为 FAIL。
2. scale：标准正文图的小黑象应是远景小执行者，实际高度约占画面 3%-5%，不能近景、笨重或抢过真实物品主视觉。看不清尺度时为 UNCLEAR。
3. text_whitelist：所有可辨认的文字必须逐字属于允许列表 {whitelist}。允许列表为空时，画面不得出现任何有意义的可读文字；乱码、伪文字、额外英文、品牌字样或 HUD 小字均为 FAIL。

返回且只返回 JSON，不要 Markdown，不要解释：
{{"status":"PASS|FAIL|BLOCKED","checks":{{"ip_lock":"PASS|FAIL|UNCLEAR","scale":"PASS|FAIL|UNCLEAR","text_whitelist":"PASS|FAIL|UNCLEAR"}},"issues":["简短问题"],"summary":"一句话结论"}}"""
    return {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "You are a strict but fast visual QA classifier. Return valid JSON only.",
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{image_b64}"},
                    },
                    {"type": "text", "text": prompt},
                ],
            },
        ],
        "thinking": {"type": "disabled"},
        "temperature": 0.1,
        "max_tokens": 1200,
    }


def response_text(response: dict[str, Any]) -> str:
    choices = response.get("choices")
    if not isinstance(choices, list) or not choices:
        return ""
    if not isinstance(choices[0], dict):
        return ""
    message = choices[0].get("message", {})
    content = message.get("content", "") if isinstance(message, dict) else ""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts: list[str] = []
        for item in content:
            if isinstance(item, dict) and isinstance(item.get("text"), str):
                parts.append(item["text"])
        return "\n".join(parts)
    return ""


def parse_json_response(text: str) -> dict[str, Any] | None:
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?\s*|\s*```$", "", cleaned, flags=re.IGNORECASE)
    try:
        value = json.loads(cleaned)
        return value if isinstance(value, dict) else None
    except json.JSONDecodeError:
        pass

    decoder = json.JSONDecoder()
    for match in re.finditer(r"\{", cleaned):
        try:
            value, _ = decoder.raw_decode(cleaned[match.start() :])
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict):
            return value
    return None


def classify(model_result: dict[str, Any], allowed_text: list[str]) -> dict[str, Any]:
    raw_checks = model_result.get("checks")
    checks: dict[str, str] = {}
    if isinstance(raw_checks, dict):
        for name in CHECK_NAMES:
            value = str(raw_checks.get(name, "UNCLEAR")).upper()
            checks[name] = value if value in CHECK_VALUES else "UNCLEAR"
    else:
        checks = {name: "UNCLEAR" for name in CHECK_NAMES}

    issues = model_result.get("issues", [])
    if not isinstance(issues, list):
        issues = [str(issues)]
    issues = [str(issue).strip() for issue in issues if str(issue).strip()]
    model_status = str(model_result.get("status", "BLOCKED")).upper()
    if model_status not in STATUS_VALUES:
        model_status = "BLOCKED"

    if any(value == "FAIL" for value in checks.values()):
        status = "FAIL"
    elif model_status == "PASS" and all(value == "PASS" for value in checks.values()):
        status = "PASS"
    else:
        status = "BLOCKED"

    if status != "PASS" and not issues:
        issues.append("一个或多个快速视觉检查未通过或无法确认")
    return {
        "status": status,
        "checks": checks,
        "issues": issues,
        "summary": str(model_result.get("summary", "")).strip(),
        "semantic_density_gate": "SEPARATE_SHOT_RECORD_GATE",
        "allowed_text": allowed_text,
    }


def result_payload(
    *,
    image: Path,
    provider: str = DEFAULT_PROVIDER,
    mode: str,
    model: str,
    endpoint: str,
    status: str,
    checks: dict[str, str] | None = None,
    issues: list[str] | None = None,
    summary: str = "",
    allowed_text: list[str] | None = None,
) -> dict[str, Any]:
    delivery = {"PASS": "DELIVER", "FAIL": "REJECT", "BLOCKED": "BLOCKED"}[status]
    return {
        "image": str(image.resolve()),
        "provider": provider,
        "mode": mode,
        "model": model,
        "endpoint": endpoint,
        "status": status,
        "delivery_status": delivery,
        "checks": checks or {name: "UNCLEAR" for name in CHECK_NAMES},
        "issues": issues or [],
        "summary": summary,
        "allowed_text": allowed_text or [],
        "semantic_density_gate": "SEPARATE_SHOT_RECORD_GATE",
    }


def exit_code(status: str) -> int:
    return {"PASS": 0, "FAIL": 1, "BLOCKED": 2}[status]


def emit(result: dict[str, Any], output: Path | None) -> None:
    rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    print(rendered, end="")
    if output:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", type=Path, help="Path to the generated body image")
    parser.add_argument(
        "--provider",
        choices=(DEFAULT_PROVIDER,),
        default=DEFAULT_PROVIDER,
        help="External provider adapter; Codex native GPT QA does not use this script",
    )
    parser.add_argument(
        "--allowed-text",
        action="append",
        default=[],
        help="One exact readable label allowed in the image; repeat as needed",
    )
    parser.add_argument(
        "--allowed-text-file",
        type=Path,
        help="UTF-8 file with one exact allowed label per line",
    )
    parser.add_argument("--mode", choices=("standard", "body"), default="standard")
    parser.add_argument("--model", default=os.environ.get("GLM_VISION_MODEL", DEFAULT_MODEL))
    parser.add_argument(
        "--endpoint",
        default=os.environ.get("GLM_VISION_URL", DEFAULT_ENDPOINT),
    )
    parser.add_argument("--max-edge", type=int, default=1280)
    parser.add_argument("--timeout", type=int, default=90)
    parser.add_argument("--output", type=Path, help="Optional JSON receipt path")
    args = parser.parse_args()

    if not args.image.is_file():
        result = result_payload(
            image=args.image,
            mode=args.mode,
            model=args.model,
            endpoint=args.endpoint,
            status="BLOCKED",
            issues=[f"图片不存在：{args.image}"],
        )
        emit(result, args.output)
        return exit_code(result["status"])
    if args.max_edge < 256 or args.timeout < 1:
        result = result_payload(
            image=args.image,
            mode=args.mode,
            model=args.model,
            endpoint=args.endpoint,
            status="BLOCKED",
            issues=["--max-edge 必须至少为 256，--timeout 必须为正数"],
        )
        emit(result, args.output)
        return exit_code(result["status"])

    if args.allowed_text_file and not args.allowed_text_file.is_file():
        result = result_payload(
            image=args.image,
            mode=args.mode,
            model=args.model,
            endpoint=args.endpoint,
            status="BLOCKED",
            issues=[f"文字白名单文件不存在：{args.allowed_text_file}"],
        )
        emit(result, args.output)
        return exit_code(result["status"])

    try:
        allowed_text = allowed_text_values(args)
    except OSError as exc:
        result = result_payload(
            image=args.image,
            mode=args.mode,
            model=args.model,
            endpoint=args.endpoint,
            status="BLOCKED",
            issues=[f"读取文字白名单失败：{safe_error(str(exc))}"],
        )
        emit(result, args.output)
        return exit_code(result["status"])
    key = load_api_key()
    if not key:
        result = result_payload(
            image=args.image,
            mode=args.mode,
            model=args.model,
            endpoint=args.endpoint,
            status="BLOCKED",
            allowed_text=allowed_text,
            issues=["未获取 GLM/ZAI API key；视觉 QA 不可用"],
        )
        emit(result, args.output)
        return exit_code(result["status"])

    image_b64, preprocessing_error = thumbnail_base64(args.image, args.max_edge)
    if preprocessing_error or not image_b64:
        result = result_payload(
            image=args.image,
            mode=args.mode,
            model=args.model,
            endpoint=args.endpoint,
            status="BLOCKED",
            allowed_text=allowed_text,
            issues=[preprocessing_error or "图片预处理失败"],
        )
        emit(result, args.output)
        return exit_code(result["status"])

    with tempfile.TemporaryDirectory(prefix="xiaohei-qa-payload-") as temp_dir:
        payload_path = Path(temp_dir) / "request.json"
        payload_path.write_text(
            json.dumps(
                build_payload(image_b64, model=args.model, allowed_text=allowed_text),
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )
        try:
            response = run_command(
                [
                    "curl",
                    "--silent",
                    "--show-error",
                    "--fail-with-body",
                    "--max-time",
                    str(args.timeout),
                    "-X",
                    "POST",
                    args.endpoint,
                    "-H",
                    f"Authorization: Bearer {key}",
                    "-H",
                    "Content-Type: application/json",
                    "--data-binary",
                    f"@{payload_path}",
                ],
                timeout=args.timeout + 5,
            )
        except (OSError, subprocess.TimeoutExpired) as exc:
            result = result_payload(
                image=args.image,
                mode=args.mode,
                model=args.model,
                endpoint=args.endpoint,
                status="BLOCKED",
                allowed_text=allowed_text,
                issues=[f"curl/GLM 请求失败：{safe_error(str(exc))}"],
            )
            emit(result, args.output)
            return exit_code(result["status"])

    if response.returncode != 0:
        detail = safe_error(response.stderr or response.stdout or "无响应")
        result = result_payload(
            image=args.image,
            mode=args.mode,
            model=args.model,
            endpoint=args.endpoint,
            status="BLOCKED",
            allowed_text=allowed_text,
            issues=[f"curl/GLM 请求失败：{detail}"],
        )
        emit(result, args.output)
        return exit_code(result["status"])

    try:
        api_response = json.loads(response.stdout)
    except json.JSONDecodeError as exc:
        result = result_payload(
            image=args.image,
            mode=args.mode,
            model=args.model,
            endpoint=args.endpoint,
            status="BLOCKED",
            allowed_text=allowed_text,
            issues=[f"GLM 返回不是合法 JSON：{safe_error(str(exc))}"],
        )
        emit(result, args.output)
        return exit_code(result["status"])

    if not isinstance(api_response, dict):
        result = result_payload(
            image=args.image,
            mode=args.mode,
            model=args.model,
            endpoint=args.endpoint,
            status="BLOCKED",
            allowed_text=allowed_text,
            issues=["GLM 返回结构不可识别"],
        )
        emit(result, args.output)
        return exit_code(result["status"])

    model_result = parse_json_response(response_text(api_response))
    if model_result is None:
        result = result_payload(
            image=args.image,
            mode=args.mode,
            model=args.model,
            endpoint=args.endpoint,
            status="BLOCKED",
            allowed_text=allowed_text,
            issues=["GLM 未返回可解析的 QA JSON"],
        )
        emit(result, args.output)
        return exit_code(result["status"])

    classified = classify(model_result, allowed_text)
    result = result_payload(
        image=args.image,
        mode=args.mode,
        model=args.model,
        endpoint=args.endpoint,
        status=classified["status"],
        checks=classified["checks"],
        issues=classified["issues"],
        summary=classified["summary"],
        allowed_text=allowed_text,
    )
    emit(result, args.output)
    return exit_code(result["status"])


if __name__ == "__main__":
    sys.exit(main())
