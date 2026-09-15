#!/usr/bin/env python3
"""Create a typography reference for one-pass Xiaohei Elephant cover generation.

This file is a model reference only. It must never be pasted onto a final cover.
"""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from PIL.PngImagePlugin import PngInfo


BRAND_FONT = Path(
    "/Users/dx/Hermes-agent/00-Agent-Core/assets/fonts/ZCOOLKuaiLe-Regular.woff2"
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_font(size: int) -> ImageFont.FreeTypeFont:
    if not BRAND_FONT.exists():
        raise SystemExit(f"未找到全局品牌字体：{BRAND_FONT}")
    return ImageFont.truetype(str(BRAND_FONT), size=size)


def fit_font(
    draw: ImageDraw.ImageDraw, text: str, max_width: int, start: int, minimum: int
) -> ImageFont.FreeTypeFont:
    for size in range(start, minimum - 1, -2):
        font = load_font(size)
        if draw.textbbox((0, 0), text, font=font)[2] <= max_width:
            return font
    raise SystemExit(f"标题过长，压缩到最多两行后再生成参考图：{text}")


def draw_highlighted(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    font: ImageFont.FreeTypeFont,
    accent_words: list[str],
) -> None:
    normal = "#20201E"
    accent = "#E8655A"
    x, y = xy
    words = sorted((word for word in accent_words if word), key=len, reverse=True)
    index = 0
    while index < len(text):
        matched = next((word for word in words if text.startswith(word, index)), None)
        chunk = matched or text[index]
        draw.text((x, y), chunk, font=font, fill=accent if matched else normal)
        x += draw.textlength(chunk, font=font)
        index += len(chunk)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output")
    parser.add_argument("--title-line", action="append", required=True)
    parser.add_argument("--accent", action="append", default=[])
    parser.add_argument("--quote", required=True)
    args = parser.parse_args()

    if len(args.title_line) > 2:
        raise SystemExit("主标题最多两行；请先压缩文案。")

    image = Image.new("RGB", (1600, 720), "#F5F0E8")
    draw = ImageDraw.Draw(image)
    left, right = 130, 1470
    y = 105

    for line in args.title_line:
        font = fit_font(draw, line, right - left, 150, 92)
        draw_highlighted(draw, (left, y), line, font, args.accent)
        box = draw.textbbox((left, y), line, font=font)
        y = box[3] + 24

    draw.line((left, y + 6, left + 760, y + 6), fill="#E8655A", width=8)
    quote_font = fit_font(draw, args.quote, right - left, 66, 46)
    draw.text((left, 585), args.quote, font=quote_font, fill="#6B6B6B")

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.suffix.lower() == ".png":
        metadata = PngInfo()
        metadata.add_text("source_role", "TYPOGRAPHY_REFERENCE_ONLY")
        metadata.add_text("font_asset", str(BRAND_FONT))
        metadata.add_text("font_sha256", sha256(BRAND_FONT))
        metadata.add_text("do_not_paste", "true")
        image.save(output, pnginfo=metadata)
    else:
        image.save(output)
    print("TYPOGRAPHY_REFERENCE_ONLY", output)
    print("FONT_ASSET", BRAND_FONT)
    print("FONT_SHA256", sha256(BRAND_FONT))
    print("REFERENCE_SHA256", sha256(output))
    print("DO_NOT_PASTE true")


if __name__ == "__main__":
    main()
