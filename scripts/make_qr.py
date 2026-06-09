#!/usr/bin/env python3
"""Generate a QR code PNG for the published dashboard URL."""

from __future__ import annotations

import argparse
from pathlib import Path

import qrcode


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ROOT / "docs" / "assets" / "qr_dashboard.png"


def main() -> None:
    parser = argparse.ArgumentParser(description="Create docs/assets/qr_dashboard.png for a dashboard URL.")
    parser.add_argument("url", help="Published GitHub Pages dashboard URL.")
    args = parser.parse_args()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    image = qrcode.make(args.url)
    image.save(OUTPUT_PATH)
    print(f"Wrote {OUTPUT_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
