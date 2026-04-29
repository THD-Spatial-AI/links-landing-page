#!/usr/bin/env python3
"""
Generate QR codes for all event pages.

Reads every */page.json in the repository root and writes:
    _site/{slug}/qr.png  — high-resolution PNG  (screen / digital poster)
    _site/{slug}/qr.svg  — scalable vector SVG   (print-ready)

Both files use the navy colour (#1B3A6B) matching the landing page design.
Error correction is set to HIGH (H) so the QR code remains scannable even
if part of it is obscured or damaged on a printed poster.

Run generate.py first to create _site/.

Usage:
    python3 scripts/generate_qr.py \\
        --site-url https://thd-spatial-ai.github.io/links-landing-page
"""

import argparse
import json
from io import BytesIO
from pathlib import Path

try:
    import qrcode
    import qrcode.constants
    import qrcode.image.svg
except ImportError:
    raise SystemExit(
        "Missing dependency.\n"
        "Install with:  pip install \"qrcode[pil]\"\n"
        "           or: pip install -r requirements.txt"
    )

ROOT  = Path(__file__).resolve().parent.parent
SITE  = ROOT / "_site"
_SKIP = frozenset({"_site", "_template", "scripts", "docs", ".github"})

_COLOR = "#1B3A6B"  # navy — matches the landing page palette


def _make_png(url: str, path: Path) -> None:
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=15,   # 15 px per module → ~570 px for a v3 code (good for 300 dpi print)
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color=_COLOR, back_color="white")
    img.save(path)


def _make_svg(url: str, path: Path) -> None:
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        image_factory=qrcode.image.svg.SvgPathImage,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image()
    buf = BytesIO()
    img.save(buf)
    svg = buf.getvalue().decode("utf-8")
    # Recolour modules from default black to navy
    svg = svg.replace('fill="#000000"', f'fill="{_COLOR}"')
    path.write_text(svg, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate QR codes for all event pages.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--site-url",
        default="https://thd-spatial-ai.github.io/links-landing-page",
        metavar="URL",
        help="GitHub Pages base URL without a trailing slash.\n"
             "Example: https://thd-spatial-ai.github.io/my-repo",
    )
    args = parser.parse_args()
    site_url = args.site_url.rstrip("/")

    if not SITE.exists():
        raise SystemExit(
            "Error: _site/ does not exist.\n"
            "Run generate.py first:  python3 scripts/generate.py"
        )

    count = 0
    for page_json in sorted(ROOT.glob("*/page.json")):
        slug = page_json.parent.name
        if slug.startswith(("_", ".")) or slug in _SKIP:
            continue

        url = f"{site_url}/{slug}/"
        out_dir = SITE / slug
        out_dir.mkdir(exist_ok=True)

        _make_png(url, out_dir / "qr.png")
        _make_svg(url, out_dir / "qr.svg")
        print(f"  {slug}/qr.png  {slug}/qr.svg  →  {url}")
        count += 1

    if count == 0:
        print("No event pages found.")
    else:
        print(f"\nDone. {count} QR code(s) written to _site/")
        print("After deployment, download them from your GitHub Pages URL:")
        print(f"  {site_url}/{{slug}}/qr.svg")
        print(f"  {site_url}/{{slug}}/qr.png")


if __name__ == "__main__":
    main()
