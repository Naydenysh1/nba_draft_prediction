#!/usr/bin/env python

from __future__ import annotations

import argparse
import re
import unicodedata
from pathlib import Path

import pandas as pd


NCAA_PATH = Path("data/pre_draft_ncaa_torvik_2008_2026_v2.csv")
REPORT_PATH = Path("data/pre_draft_ncaa_torvik_sanity_check.md")

CHECK_PLAYERS = [
    ("zion williamson", 2019, True),
    ("ja morant", 2019, True),
    ("rj barrett", 2019, True),
    ("de andre hunter", 2019, True),
    ("anthony edwards", 2020, True),
    ("lamelo ball", 2020, False),
    ("cade cunningham", 2021, True),
    ("evan mobley", 2021, True),
    ("jalen green", 2021, False),
    ("paolo banchero", 2022, True),
    ("chet holmgren", 2022, True),
    ("jabari smith", 2022, True),
    ("victor wembanyama", 2023, False),
    ("brandon miller", 2023, True),
    ("scoot henderson", 2023, False),
    ("zach edey", 2024, True),
    ("reed sheppard", 2024, True),
    ("alexandre sarr", 2024, False),
    ("cooper flagg", 2025, True),
    ("ace bailey", 2025, True),
    ("dylan harper", 2025, True),
]

KEY_COLUMNS = [
    "name",
    "draft_year",
    "ncaa_player_raw",
    "ncaa_team",
    "ncaa_conf",
    "ncaa_pos",
    "ncaa_height",
    "ncaa_games",
    "ncaa_mpg",
    "ncaa_ppg",
    "ncaa_rpg",
    "ncaa_apg",
    "ncaa_spg",
    "ncaa_bpg",
    "ncaa_fg_pct",
    "ncaa_two_pct",
    "ncaa_three_pct",
    "ncaa_ft_pct",
    "ncaa_usage",
    "ncaa_bpm",
]

NUMERIC_COLUMNS = [
    "draft_year",
    "ncaa_games",
    "ncaa_mpg",
    "ncaa_ppg",
    "ncaa_rpg",
    "ncaa_apg",
    "ncaa_spg",
    "ncaa_bpg",
    "ncaa_fg_pct",
    "ncaa_two_pct",
    "ncaa_three_pct",
    "ncaa_ft_pct",
    "ncaa_usage",
    "ncaa_bpm",
]

MISSINGNESS_COLUMNS = [
    "ncaa_mpg",
    "ncaa_ppg",
    "ncaa_rpg",
    "ncaa_apg",
    "ncaa_fg_pct",
    "ncaa_two_pct",
    "ncaa_three_pct",
    "ncaa_ft_pct",
    "ncaa_usage",
    "ncaa_bpm",
]


def clean_name(value: object) -> str:
    text = "" if pd.isna(value) else str(value)
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = text.lower()
    text = re.sub(r"\b(jr|sr|ii|iii|iv|v)\b\.?", "", text)
    text = re.sub(r"[^a-z0-9 ]+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def compact_initial_tokens(value: str) -> str:
    tokens = value.split()
    compacted: list[str] = []
    idx = 0
    while idx < len(tokens):
      if len(tokens[idx]) == 1:
          start = idx
          while idx < len(tokens) and len(tokens[idx]) == 1:
              idx += 1
          compacted.append("".join(tokens[start:idx]))
      else:
          compacted.append(tokens[idx])
          idx += 1
    return " ".join(compacted)


def yes_no(value: bool) -> str:
    return "yes" if value else "no"


def format_value(value: object) -> str:
    if pd.isna(value):
        return ""
    if isinstance(value, float):
        return f"{value:.4f}".rstrip("0").rstrip(".")
    return str(value)


def markdown_table(df: pd.DataFrame) -> str:
    if df.empty:
        return "_None_"
    rendered = df.copy()
    for col in rendered.columns:
        rendered[col] = rendered[col].map(format_value)

    headers = [str(col) for col in rendered.columns]
    rows = rendered.astype(str).values.tolist()
    widths = [
        max(len(headers[idx]), *(len(row[idx]) for row in rows))
        for idx in range(len(headers))
    ]

    def render_row(values: list[str]) -> str:
        cells = [values[idx].ljust(widths[idx]) for idx in range(len(values))]
        return "| " + " | ".join(cells) + " |"

    separator = "| " + " | ".join("-" * width for width in widths) + " |"
    return "\n".join([render_row(headers), separator, *[render_row(row) for row in rows]])


def build_report(ncaa_path: Path, report_path: Path) -> dict[str, object]:
    df = pd.read_csv(ncaa_path)

    if "name" not in df.columns:
        raise ValueError("NCAA CSV is missing required column: name")
    if "draft_year" not in df.columns:
        raise ValueError("NCAA CSV is missing required column: draft_year")

    df["__clean_name_check"] = df["name"].map(clean_name)
    df["__compact_name_check"] = df["__clean_name_check"].map(compact_initial_tokens)
    df["draft_year"] = pd.to_numeric(df["draft_year"], errors="coerce").astype("Int64")

    player_rows = []
    found_detail_rows = []
    suspicious_cases = []

    for raw_name, draft_year, expected_present in CHECK_PLAYERS:
        cleaned = clean_name(raw_name)
        compacted = compact_initial_tokens(cleaned)
        matches = df[
            (df["__clean_name_check"] == cleaned)
            & (df["draft_year"] == draft_year)
        ].copy()
        match_method = "exact_clean_name"
        if matches.empty:
            matches = df[
                (df["__compact_name_check"] == compacted)
                & (df["draft_year"] == draft_year)
            ].copy()
            match_method = "initials_compact" if not matches.empty else "not_found"
        found = not matches.empty
        status = "ok" if found == expected_present else "suspicious"

        if status == "suspicious":
            suspicious_cases.append(f"{raw_name} ({draft_year})")

        player_rows.append(
            {
                "queried_raw_name": raw_name,
                "cleaned_name": cleaned,
                "draft_year": draft_year,
                "found_in_ncaa_csv": yes_no(found),
                "expected_presence": yes_no(expected_present),
                "status": status,
                "match_method": match_method,
            }
        )

        if found:
            out = matches[KEY_COLUMNS].head(5).copy()
            out.insert(0, "queried_raw_name", raw_name)
            found_detail_rows.append(out)

    checked_df = pd.DataFrame(player_rows)
    found_details = (
        pd.concat(found_detail_rows, ignore_index=True)
        if found_detail_rows
        else pd.DataFrame(columns=["queried_raw_name", *KEY_COLUMNS])
    )

    duplicate_groups = (
        df.groupby(["name", "draft_year"], dropna=False)
        .size()
        .reset_index(name="rows")
        .query("rows > 1")
        .sort_values(["rows", "draft_year", "name"], ascending=[False, True, True])
    )

    expected_years = set(range(2008, 2027))
    actual_years = set(df["draft_year"].dropna().astype(int).unique())
    missing_years = sorted(expected_years - actual_years)
    extra_years = sorted(actual_years - expected_years)

    key_column_check = pd.DataFrame(
        {
            "column": KEY_COLUMNS,
            "present": [yes_no(col in df.columns) for col in KEY_COLUMNS],
        }
    )

    numeric_check_rows = []
    for col in NUMERIC_COLUMNS:
        if col not in df.columns:
            numeric_check_rows.append(
                {"column": col, "present": "no", "numeric": "no", "non_numeric_values": ""}
            )
            continue
        converted = pd.to_numeric(df[col], errors="coerce")
        original_non_missing = df[col].notna()
        non_numeric = original_non_missing & converted.isna()
        examples = df.loc[non_numeric, col].astype(str).drop_duplicates().head(5).tolist()
        numeric_check_rows.append(
            {
                "column": col,
                "present": "yes",
                "numeric": yes_no(not non_numeric.any()),
                "non_numeric_values": ", ".join(examples),
            }
        )
    numeric_check = pd.DataFrame(numeric_check_rows)

    missing_rows = []
    for col in MISSINGNESS_COLUMNS:
        if col not in df.columns:
            missing_pct = 100.0
        else:
            missing_pct = df[col].isna().mean() * 100
        missing_rows.append({"column": col, "missing_pct": round(missing_pct, 2)})
    missingness = pd.DataFrame(missing_rows).sort_values("missing_pct", ascending=False)

    summary = {
        "checked_players": len(CHECK_PLAYERS),
        "found": int((checked_df["found_in_ncaa_csv"] == "yes").sum()),
        "missing_as_expected": int(
            ((checked_df["found_in_ncaa_csv"] == "no") & (checked_df["expected_presence"] == "no")).sum()
        ),
        "suspicious": int((checked_df["status"] == "suspicious").sum()),
        "suspicious_cases": suspicious_cases,
    }

    report_lines = [
        "# NCAA Torvik Sanity Check",
        "",
        "## Summary",
        "",
        markdown_table(
            pd.DataFrame(
                [
                    {"metric": "rows", "value": len(df)},
                    {"metric": "columns", "value": len([c for c in df.columns if not c.startswith('__')])},
                    {"metric": "checked_players", "value": summary["checked_players"]},
                    {"metric": "found_checked_players", "value": summary["found"]},
                    {"metric": "missing_as_expected", "value": summary["missing_as_expected"]},
                    {"metric": "suspicious_cases", "value": summary["suspicious"]},
                ]
            )
        ),
        "",
        "## Checked Prospects",
        "",
        markdown_table(checked_df),
        "",
        "## Found Prospect Detail Rows",
        "",
        markdown_table(found_details),
        "",
        "## Duplicate name + draft_year Rows",
        "",
        f"Duplicate groups: {len(duplicate_groups)}",
        "",
        markdown_table(duplicate_groups.head(50)),
        "",
        "## Year Coverage",
        "",
        f"Expected years present: {yes_no(not missing_years and not extra_years)}",
        "",
        f"Missing years: {', '.join(map(str, missing_years)) if missing_years else 'None'}",
        "",
        f"Extra years: {', '.join(map(str, extra_years)) if extra_years else 'None'}",
        "",
        "## Key Columns Present",
        "",
        markdown_table(key_column_check),
        "",
        "## Numeric Column Checks",
        "",
        markdown_table(numeric_check),
        "",
        "## Missing-Value Percentages",
        "",
        markdown_table(missingness),
        "",
    ]

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(report_lines), encoding="utf-8")
    return summary


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ncaa", default=str(NCAA_PATH))
    parser.add_argument("--report", default=str(REPORT_PATH))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    summary = build_report(Path(args.ncaa), Path(args.report))
    print(f"Checked players: {summary['checked_players']}")
    print(f"Found: {summary['found']}")
    print(f"Missing as expected: {summary['missing_as_expected']}")
    print(f"Suspicious: {summary['suspicious']}")
    if summary["suspicious_cases"]:
        print("Suspicious cases:")
        for case in summary["suspicious_cases"]:
            print(f"- {case}")
    else:
        print("Suspicious cases: None")


if __name__ == "__main__":
    main()
