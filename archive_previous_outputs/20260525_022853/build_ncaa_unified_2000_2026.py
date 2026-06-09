#!/usr/bin/env python3
"""
Unify two standalone NCAA data layers into one clean NCAA dataset.

Inputs:
    data/pre_draft_ncaa_sportsref_2000_2007.csv
    data/pre_draft_ncaa_torvik_2008_2026_v2.csv

Output:
    data/pre_draft_ncaa_unified_2000_2026.csv
    data/pre_draft_ncaa_unified_report.md

Important:
- This script does NOT merge NCAA data with the NBA Draft/Combine dataset.
- This script does NOT create draft_tier.
- This script does NOT impute missing values.
- This script only standardizes schemas and stacks two NCAA sources.
"""

from __future__ import annotations

import argparse
import re
import unicodedata
from pathlib import Path
from typing import Iterable

import numpy as np
import pandas as pd

FINAL_COLUMNS = [
    "name",
    "draft_year",
    "ncaa_source",
    "ncaa_player_raw",
    "ncaa_team",
    "ncaa_conf",
    "ncaa_pos",
    "ncaa_exp",
    "ncaa_height",
    "ncaa_games",
    "ncaa_mpg",
    "ncaa_ppg",
    "ncaa_fg_pct",
    "ncaa_two_pct",
    "ncaa_three_pct",
    "ncaa_ft_pct",
    "ncaa_oreb",
    "ncaa_dreb",
    "ncaa_rpg",
    "ncaa_apg",
    "ncaa_ast_to",
    "ncaa_spg",
    "ncaa_bpg",
    "ncaa_tpg",
    "ncaa_ortg",
    "ncaa_adj_oe",
    "ncaa_drtg",
    "ncaa_porpag",
    "ncaa_dporpag",
    "ncaa_bpm",
    "ncaa_obpm",
    "ncaa_dbpm",
    "ncaa_usage",
]

NUMERIC_COLUMNS = [
    "draft_year",
    "ncaa_games",
    "ncaa_mpg",
    "ncaa_ppg",
    "ncaa_fg_pct",
    "ncaa_two_pct",
    "ncaa_three_pct",
    "ncaa_ft_pct",
    "ncaa_oreb",
    "ncaa_dreb",
    "ncaa_rpg",
    "ncaa_apg",
    "ncaa_ast_to",
    "ncaa_spg",
    "ncaa_bpg",
    "ncaa_tpg",
    "ncaa_ortg",
    "ncaa_adj_oe",
    "ncaa_drtg",
    "ncaa_porpag",
    "ncaa_dporpag",
    "ncaa_bpm",
    "ncaa_obpm",
    "ncaa_dbpm",
    "ncaa_usage",
]


def clean_name(name: object) -> str:
    if pd.isna(name):
        return ""
    s = str(name).strip().lower()
    s = unicodedata.normalize("NFKD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = re.sub(r"\b(jr|sr|ii|iii|iv|v)\b\.?", "", s)
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def to_numeric(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series.astype(str).str.replace("%", "", regex=False), errors="coerce")


def ensure_columns(df: pd.DataFrame, columns: Iterable[str]) -> pd.DataFrame:
    out = df.copy()
    for col in columns:
        if col not in out.columns:
            out[col] = pd.NA
    return out


def load_sportsref(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)

    rename = {
        "sportsref_player_raw": "ncaa_player_raw",
        "sportsref_school": "ncaa_team",
        "sportsref_conf": "ncaa_conf",
        "sportsref_games": "ncaa_games",
        "sportsref_mpg": "ncaa_mpg",
        "sportsref_ppg": "ncaa_ppg",
        "sportsref_rpg": "ncaa_rpg",
        "sportsref_apg": "ncaa_apg",
        "sportsref_spg": "ncaa_spg",
        "sportsref_bpg": "ncaa_bpg",
        "sportsref_tpg": "ncaa_tpg",
        "sportsref_fg_pct": "ncaa_fg_pct",
        "sportsref_two_pct": "ncaa_two_pct",
        "sportsref_three_pct": "ncaa_three_pct",
        "sportsref_ft_pct": "ncaa_ft_pct",
    }
    df = df.rename(columns=rename)
    df["ncaa_source"] = "sports_reference"

    # Sports-Reference targeted layer does not contain these Torvik-only fields.
    df = ensure_columns(df, FINAL_COLUMNS)
    return df[FINAL_COLUMNS]


def load_torvik(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["ncaa_source"] = "torvik"
    df = ensure_columns(df, FINAL_COLUMNS)
    return df[FINAL_COLUMNS]


def standardize_types(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["name"] = out["name"].map(clean_name)

    for col in NUMERIC_COLUMNS:
        if col in out.columns:
            out[col] = to_numeric(out[col])

    out["draft_year"] = out["draft_year"].astype("Int64")

    text_cols = [c for c in FINAL_COLUMNS if c not in NUMERIC_COLUMNS]
    for col in text_cols:
        out[col] = out[col].replace({np.nan: pd.NA})

    return out


def resolve_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Keep one name+draft_year row. Prefer more complete/high-minutes rows."""
    out = df.copy()
    out["_source_priority"] = out["ncaa_source"].map({"sports_reference": 1, "torvik": 1}).fillna(9)
    out["_nonnull_count"] = out[FINAL_COLUMNS].notna().sum(axis=1)

    out = out.sort_values(
        by=["name", "draft_year", "_source_priority", "ncaa_mpg", "ncaa_games", "_nonnull_count"],
        ascending=[True, True, True, False, False, False],
        na_position="last",
    )
    out = out.drop_duplicates(subset=["name", "draft_year"], keep="first")
    out = out.drop(columns=["_source_priority", "_nonnull_count"])
    return out.reset_index(drop=True)


def validate_years(df: pd.DataFrame, start_year: int, end_year: int) -> tuple[list[int], list[int]]:
    expected = set(range(start_year, end_year + 1))
    observed = set(df["draft_year"].dropna().astype(int).unique())
    missing = sorted(expected - observed)
    extra = sorted(observed - expected)
    return missing, extra


def write_report(
    unified: pd.DataFrame,
    before_dedup: pd.DataFrame,
    sportsref: pd.DataFrame,
    torvik: pd.DataFrame,
    report_path: Path,
    start_year: int,
    end_year: int,
) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)

    missing_years, extra_years = validate_years(unified, start_year, end_year)
    duplicate_count = unified.duplicated(subset=["name", "draft_year"]).sum()
    exact_columns = list(unified.columns) == FINAL_COLUMNS

    rows_by_year = unified.groupby("draft_year").size().rename("rows").reset_index()
    rows_by_source = unified.groupby("ncaa_source").size().rename("rows").reset_index()
    rows_by_source_year = (
        unified.groupby(["draft_year", "ncaa_source"]).size().rename("rows").reset_index()
    )

    numeric_missing = (
        unified[NUMERIC_COLUMNS]
        .isna()
        .mean()
        .mul(100)
        .round(1)
        .sort_values(ascending=False)
        .rename("missing_pct")
        .reset_index()
        .rename(columns={"index": "column"})
    )

    non_numeric = []
    for col in NUMERIC_COLUMNS:
        if col in unified.columns:
            numeric_ok = pd.api.types.is_numeric_dtype(unified[col]) or str(unified[col].dtype) == "Int64"
            non_numeric.append({"column": col, "numeric_ok": numeric_ok, "dtype": str(unified[col].dtype)})
    numeric_check = pd.DataFrame(non_numeric)

    overlap_rows = before_dedup.duplicated(subset=["name", "draft_year"], keep=False).sum()

    lines = []
    lines.append("# Unified NCAA Dataset Report")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    summary = pd.DataFrame(
        [
            ["start_year", start_year],
            ["end_year", end_year],
            ["sportsref_input_rows", len(sportsref)],
            ["torvik_input_rows", len(torvik)],
            ["rows_before_duplicate_resolution", len(before_dedup)],
            ["rows_after_duplicate_resolution", len(unified)],
            ["columns", len(unified.columns)],
            ["final_columns_exact", exact_columns],
            ["duplicate_name_draft_year_rows_after_resolution", duplicate_count],
            ["overlap_name_draft_year_rows_before_resolution", int(overlap_rows)],
            ["missing_years", "None" if not missing_years else ", ".join(map(str, missing_years))],
            ["extra_years", "None" if not extra_years else ", ".join(map(str, extra_years))],
        ],
        columns=["metric", "value"],
    )
    lines.append(summary.to_markdown(index=False))
    lines.append("")

    lines.append("## Rows By draft_year")
    lines.append("")
    lines.append(rows_by_year.to_markdown(index=False))
    lines.append("")

    lines.append("## Rows By Source")
    lines.append("")
    lines.append(rows_by_source.to_markdown(index=False))
    lines.append("")

    lines.append("## Rows By draft_year And Source")
    lines.append("")
    lines.append(rows_by_source_year.to_markdown(index=False))
    lines.append("")

    lines.append("## Numeric Column Checks")
    lines.append("")
    lines.append(numeric_check.to_markdown(index=False))
    lines.append("")

    lines.append("## Missing-Value Percentage For Numeric Columns")
    lines.append("")
    lines.append(numeric_missing.to_markdown(index=False))
    lines.append("")

    lines.append("## Columns")
    lines.append("")
    for col in unified.columns:
        lines.append(f"- {col}")
    lines.append("")

    lines.append("## First 30 Rows")
    lines.append("")
    lines.append(unified.head(30).to_markdown(index=False))
    lines.append("")

    report_path.write_text("\n".join(lines), encoding="utf-8")


def build_unified(args: argparse.Namespace) -> pd.DataFrame:
    sportsref = load_sportsref(Path(args.sportsref))
    torvik = load_torvik(Path(args.torvik))

    sportsref = standardize_types(sportsref)
    torvik = standardize_types(torvik)

    # Enforce intended year ranges so the unified dataset has a clean source split.
    sportsref = sportsref[sportsref["draft_year"].between(args.start_year, args.sportsref_end_year)].copy()
    torvik = torvik[torvik["draft_year"].between(args.torvik_start_year, args.end_year)].copy()

    before_dedup = pd.concat([sportsref, torvik], ignore_index=True, sort=False)[FINAL_COLUMNS]
    unified = resolve_duplicates(before_dedup)
    unified = unified.sort_values(["draft_year", "name"]).reset_index(drop=True)
    return unified, before_dedup, sportsref, torvik


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sportsref", default="data/pre_draft_ncaa_sportsref_2000_2007.csv")
    parser.add_argument("--torvik", default="data/pre_draft_ncaa_torvik_2008_2026_v2.csv")
    parser.add_argument("--out", default="data/pre_draft_ncaa_unified_2000_2026.csv")
    parser.add_argument("--report", default="data/pre_draft_ncaa_unified_report.md")
    parser.add_argument("--start-year", type=int, default=2000)
    parser.add_argument("--sportsref-end-year", type=int, default=2007)
    parser.add_argument("--torvik-start-year", type=int, default=2008)
    parser.add_argument("--end-year", type=int, default=2026)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    out_path = Path(args.out)
    report_path = Path(args.report)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    unified, before_dedup, sportsref, torvik = build_unified(args)
    unified.to_csv(out_path, index=False)
    write_report(
        unified=unified,
        before_dedup=before_dedup,
        sportsref=sportsref,
        torvik=torvik,
        report_path=report_path,
        start_year=args.start_year,
        end_year=args.end_year,
    )

    print(f"Saved unified NCAA CSV: {out_path}")
    print(f"Saved report: {report_path}")
    print(f"Rows: {len(unified)}")
    print(f"Columns: {len(unified.columns)}")
    print("Rows by source:")
    print(unified.groupby("ncaa_source").size())


if __name__ == "__main__":
    main()
