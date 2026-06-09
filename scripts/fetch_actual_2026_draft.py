#!/usr/bin/env python3
"""
Future-ready placeholder for fetching the real 2026 NBA Draft results.

This script intentionally does not create fake data. The project currently has
archived NBA Stats API usage for historical metadata, but no active, reliable
draft-results fetcher in scripts/. After the 2026 draft, implement the fetch
logic here and write data/final/actual_draft_2026.csv with:

    name,overall_pick

Undrafted players may be omitted or written with overall_pick 999. The dashboard
builder treats players missing from actual results as undrafted when the actual
file exists.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ROOT / "data" / "final" / "actual_draft_2026.csv"


def main() -> None:
    print("No actual 2026 draft fetch has been implemented yet.")
    print("After the real draft, add reliable fetch logic here or create this file manually:")
    print(f"  {OUTPUT_PATH.relative_to(ROOT)}")
    print("Required columns: name,overall_pick")


if __name__ == "__main__":
    main()
