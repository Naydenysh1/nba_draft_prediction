#!/usr/bin/env python3
"""
Inspect how well the unified NCAA layer matches the clean NBA Draft + Combine base.

Inputs:
    data/nba_draft_combine_clean_2000_2026.csv
    data/pre_draft_ncaa_unified_2000_2026.csv

Output:
    data/nba_draft_ncaa_merge_report.md

Important:
- This script does NOT save a merged CSV.
- This script does NOT create draft_tier.
- This script does NOT impute missing values.
- This script only creates a diagnostic report for deciding whether the merge is safe.
"""

from __future__ import annotations

import argparse
import re
import unicodedata
from pathlib import Path

import numpy as np
import pandas as pd

try:
    from rapidfuzz import fuzz, process
except ImportError:  # optional, script still works without fuzzy examples
    fuzz = None
    process = None


KEY_COLS = ["name", "draft_year"]
NCAA_FEATURE_COLS = [
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

MANUAL_ALIASES = {
    ("wesley johnson", 2010): "wes johnson",
    ("enes freedom", 2011): "enes kanter",
    ("maurice harkless", 2012): "moe harkless",
    ("devyn marble", 2014): "roy devyn marble",
    ("bam adebayo", 2017): "edrice adebayo",
    ("t j leaf", 2017): "tj leaf",
    ("wes iwundu", 2017): "wesley iwundu",
    ("mo bamba", 2018): "amidou bamba",
    ("svi mykhailiuk", 2018): "sviatoslav mykhailiuk",
    ("nic claxton", 2019): "nicolas claxton",
    ("vj edgecombe", 2025): "j edgecombe",
}

MANUAL_ALIAS_CHECKS = list(MANUAL_ALIASES.keys())


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


def compact_initials(name: object) -> str:
    cleaned = clean_name(name)
    tokens = cleaned.split()
    if len(tokens) < 3:
        return cleaned

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


def spaced_initials(name: object) -> str:
    cleaned = clean_name(name)
    tokens = cleaned.split()
    if len(tokens) < 2:
        return cleaned
    first = tokens[0]
    if len(first) == 2 and first.isalpha():
        return " ".join([first[0], first[1], *tokens[1:]])
    return cleaned


def add_name_keys(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["name_clean"] = out["name"].map(clean_name)
    out["name_compact_initials"] = out["name_clean"].map(compact_initials)
    out["name_spaced_initials"] = out["name_clean"].map(spaced_initials)
    return out


def add_manual_alias_key(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()

    def alias_for_row(row: pd.Series) -> str:
        year = row.get("draft_year")
        if pd.isna(year):
            return row["name_clean"]
        key = (row["name_clean"], int(year))
        return clean_name(MANUAL_ALIASES.get(key, row["name_clean"]))

    out["name_manual_alias"] = out.apply(alias_for_row, axis=1)
    return out


def add_pick_group(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    pick = pd.to_numeric(out["overall_pick"], errors="coerce")

    conditions = [
        out["draft_year"].eq(2026) & pick.isna(),
        pick.eq(999),
        pick.between(1, 5),
        pick.between(6, 14),
        pick.between(15, 30),
        pick.between(31, 998),
    ]
    choices = [
        "prediction_2026_unknown",
        "undrafted_999",
        "top_5",
        "picks_6_14",
        "picks_15_30",
        "second_round",
    ]
    out["draft_group_preview"] = np.select(conditions, choices, default="unknown")
    return out


def make_ncaa_lookup(ncaa: pd.DataFrame, key_col: str) -> pd.DataFrame:
    feature_cols = [col for col in NCAA_FEATURE_COLS if col in ncaa.columns]
    lookup_cols = [key_col, "draft_year", *feature_cols]
    lookup = ncaa[lookup_cols].dropna(subset=[key_col, "draft_year"]).copy()
    lookup = lookup.drop_duplicates(subset=[key_col, "draft_year"], keep="first")
    rename = {key_col: "_join_name_key"}
    rename.update({col: f"{col}__candidate" for col in feature_cols})
    return lookup.rename(columns=rename)


def apply_join_pass(
    merged: pd.DataFrame,
    ncaa: pd.DataFrame,
    base_key_col: str,
    ncaa_key_col: str,
    method: str,
) -> tuple[pd.DataFrame, int]:
    feature_cols = [col for col in NCAA_FEATURE_COLS if col in merged.columns]
    lookup = make_ncaa_lookup(ncaa, ncaa_key_col)
    pass_df = merged[["_base_row_id", base_key_col, "draft_year"]].rename(
        columns={base_key_col: "_join_name_key"}
    )
    pass_df = pass_df.merge(lookup, on=["_join_name_key", "draft_year"], how="left")

    candidate_source = "ncaa_source__candidate"
    eligible = merged["ncaa_match_method"].eq("unmatched") & pass_df[candidate_source].notna()
    add_count = int(eligible.sum())
    if add_count == 0:
        candidate_cols = [c for c in pass_df.columns if c.endswith("__candidate")]
        return merged.drop(columns=[c for c in candidate_cols if c in merged.columns], errors="ignore"), 0

    for col in feature_cols:
        candidate_col = f"{col}__candidate"
        if candidate_col in pass_df.columns:
            merged.loc[eligible, col] = pass_df.loc[eligible, candidate_col].values
    merged.loc[eligible, "ncaa_match_method"] = method
    merged["has_ncaa_match"] = merged["ncaa_match_method"].ne("unmatched")
    return merged, add_count


def diagnostic_left_join(base: pd.DataFrame, ncaa: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, int]]:
    base_work = base.copy().reset_index(drop=True)
    ncaa_work = ncaa.copy().reset_index(drop=True)
    base_work["_base_row_id"] = np.arange(len(base_work))

    for col in NCAA_FEATURE_COLS:
        if col not in base_work.columns:
            base_work[col] = pd.NA

    base_work["ncaa_match_method"] = "unmatched"
    base_work["has_ncaa_match"] = False

    merged, exact_count = apply_join_pass(
        base_work,
        ncaa_work,
        base_key_col="name_clean",
        ncaa_key_col="name_clean",
        method="exact_name",
    )
    merged, compact_count = apply_join_pass(
        merged,
        ncaa_work,
        base_key_col="name_compact_initials",
        ncaa_key_col="name_compact_initials",
        method="compact_initials",
    )
    merged, spaced_count = apply_join_pass(
        merged,
        ncaa_work,
        base_key_col="name_spaced_initials",
        ncaa_key_col="name_spaced_initials",
        method="spaced_initials",
    )
    merged, manual_alias_count = apply_join_pass(
        merged,
        ncaa_work,
        base_key_col="name_manual_alias",
        ncaa_key_col="name_clean",
        method="manual_alias",
    )

    counts = {
        "exact_name_matches": exact_count,
        "compact_initials_matches": compact_count,
        "spaced_initials_matches": spaced_count,
        "initials_improved_matches": exact_count + compact_count + spaced_count,
        "manual_alias_matches": manual_alias_count,
        "improved_matches": exact_count + compact_count + spaced_count + manual_alias_count,
    }
    return merged, counts


def match_rate_table(df: pd.DataFrame, group_cols: list[str]) -> pd.DataFrame:
    if not group_cols:
        total = len(df)
        matched = int(df["has_ncaa_match"].sum())
        return pd.DataFrame(
            [{
                "group": "overall",
                "rows": total,
                "matched": matched,
                "unmatched": total - matched,
                "match_rate_pct": round(matched / total * 100, 1) if total else 0.0,
            }]
        )

    table = (
        df.groupby(group_cols, dropna=False)
        .agg(rows=("has_ncaa_match", "size"), matched=("has_ncaa_match", "sum"))
        .reset_index()
    )
    table["matched"] = table["matched"].astype(int)
    table["unmatched"] = table["rows"] - table["matched"]
    table["match_rate_pct"] = (table["matched"] / table["rows"] * 100).round(1)
    return table.sort_values(group_cols).reset_index(drop=True)


def make_fuzzy_candidates(unmatched: pd.DataFrame, ncaa: pd.DataFrame, limit: int = 50) -> pd.DataFrame:
    if fuzz is None or process is None or unmatched.empty:
        return pd.DataFrame()

    rows = []
    for _, row in unmatched.head(limit).iterrows():
        year = row["draft_year"]
        name = row["name"]
        same_year = ncaa[ncaa["draft_year"].eq(year)]
        choices = same_year["name"].dropna().unique().tolist()
        if not choices:
            rows.append({
                "name": name,
                "draft_year": year,
                "organization": row.get("organization", pd.NA),
                "best_ncaa_name_candidate": pd.NA,
                "candidate_score": pd.NA,
                "candidate_team": pd.NA,
            })
            continue
        best = process.extractOne(name, choices, scorer=fuzz.WRatio)
        if best is None:
            continue
        candidate_name, score, _ = best
        candidate_row = same_year[same_year["name"].eq(candidate_name)].head(1)
        candidate_team = candidate_row["ncaa_team"].iloc[0] if not candidate_row.empty and "ncaa_team" in candidate_row else pd.NA
        rows.append({
            "name": name,
            "draft_year": year,
            "organization": row.get("organization", pd.NA),
            "overall_pick": row.get("overall_pick", pd.NA),
            "best_ncaa_name_candidate": candidate_name,
            "candidate_score": score,
            "candidate_team": candidate_team,
        })
    return pd.DataFrame(rows)


def make_manual_alias_status(merged: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for base_name, draft_year in MANUAL_ALIAS_CHECKS:
        candidate = merged[
            merged["name_clean"].eq(base_name)
            & merged["draft_year"].eq(draft_year)
        ].head(1)
        if candidate.empty:
            rows.append(
                {
                    "base_name": base_name,
                    "draft_year": draft_year,
                    "alias_name": MANUAL_ALIASES[(base_name, draft_year)],
                    "matched": False,
                    "ncaa_match_method": "missing_base_row",
                    "ncaa_player_raw": pd.NA,
                    "ncaa_team": pd.NA,
                }
            )
            continue
        row = candidate.iloc[0]
        rows.append(
            {
                "base_name": base_name,
                "draft_year": draft_year,
                "alias_name": MANUAL_ALIASES[(base_name, draft_year)],
                "matched": bool(row["has_ncaa_match"]),
                "ncaa_match_method": row["ncaa_match_method"],
                "ncaa_player_raw": row.get("ncaa_player_raw", pd.NA),
                "ncaa_team": row.get("ncaa_team", pd.NA),
            }
        )
    return pd.DataFrame(rows)


def safe_to_markdown(df: pd.DataFrame, index: bool = False) -> str:
    if df is None or df.empty:
        return "_None_"
    return df.to_markdown(index=index)


def write_report(
    base: pd.DataFrame,
    ncaa: pd.DataFrame,
    merged: pd.DataFrame,
    fuzzy_candidates: pd.DataFrame,
    report_path: Path,
    match_counts: dict[str, int],
) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)

    base_dupes = int(base.duplicated(subset=["name", "draft_year", "overall_pick"]).sum())
    ncaa_dupes = int(ncaa.duplicated(subset=["name", "draft_year"]).sum())
    merged_row_count_ok = len(base) == len(merged)
    matched = int(merged["has_ncaa_match"].sum())
    total = len(merged)
    match_rate = round(matched / total * 100, 1) if total else 0.0
    exact_name_matches = int(match_counts.get("exact_name_matches", 0))
    compact_initials_matches = int(match_counts.get("compact_initials_matches", 0))
    spaced_initials_matches = int(match_counts.get("spaced_initials_matches", 0))
    initials_improved_matches = int(match_counts.get("initials_improved_matches", 0))
    manual_alias_matches = int(match_counts.get("manual_alias_matches", 0))
    improved_matches = int(match_counts.get("improved_matches", matched))
    alternate_key_matches = compact_initials_matches + spaced_initials_matches

    college = merged[merged["organization_type"].eq("College/University")].copy()
    college_matched = int(college["has_ncaa_match"].sum())
    college_rate = round(college_matched / len(college) * 100, 1) if len(college) else 0.0

    prediction_2026 = merged[merged["draft_year"].eq(2026)].copy()
    prediction_2026_matched = int(prediction_2026["has_ncaa_match"].sum())
    prediction_2026_rate = round(prediction_2026_matched / len(prediction_2026) * 100, 1) if len(prediction_2026) else 0.0

    ncaa_cols_present = [c for c in NCAA_FEATURE_COLS if c in merged.columns]
    ncaa_missing = (
        merged[ncaa_cols_present]
        .isna()
        .mean()
        .mul(100)
        .round(1)
        .sort_values(ascending=False)
        .rename("missing_pct")
        .reset_index()
        .rename(columns={"index": "column"})
    )

    summary = pd.DataFrame(
        [
            ["base_rows", len(base)],
            ["base_columns", len(base.columns)],
            ["ncaa_rows", len(ncaa)],
            ["ncaa_columns", len(ncaa.columns)],
            ["merged_rows_for_report", len(merged)],
            ["merged_row_count_equals_base", merged_row_count_ok],
            ["base_duplicate_name_draft_year_pick_rows", base_dupes],
            ["ncaa_duplicate_name_draft_year_rows", ncaa_dupes],
            ["old_exact_name_match_count", exact_name_matches],
            ["matches_after_initials_matching", initials_improved_matches],
            ["additional_matches_from_alternate_keys", alternate_key_matches],
            ["additional_matches_from_compact_initials", compact_initials_matches],
            ["additional_matches_from_spaced_initials", spaced_initials_matches],
            ["additional_matches_from_manual_alias", manual_alias_matches],
            ["final_improved_match_count", improved_matches],
            ["matched_rows", matched],
            ["unmatched_rows", total - matched],
            ["match_rate_pct", match_rate],
            ["college_university_rows", len(college)],
            ["college_university_matched", college_matched],
            ["college_university_match_rate_pct", college_rate],
            ["prediction_2026_rows", len(prediction_2026)],
            ["prediction_2026_matched", prediction_2026_matched],
            ["prediction_2026_match_rate_pct", prediction_2026_rate],
        ],
        columns=["metric", "value"],
    )

    by_year = match_rate_table(merged, ["draft_year"])
    by_org_type = match_rate_table(merged, ["organization_type"])
    by_group = match_rate_table(merged, ["draft_group_preview"])
    by_method = merged.groupby("ncaa_match_method", dropna=False).size().rename("rows").reset_index()
    by_year_org_type = match_rate_table(merged, ["draft_year", "organization_type"])
    manual_alias_status = make_manual_alias_status(merged)

    unmatched_college_examples = (
        merged[
            merged["organization_type"].eq("College/University")
            & ~merged["has_ncaa_match"]
        ][[
            "name", "draft_year", "overall_pick", "draft_group_preview", "organization",
            "organization_type", "position"
        ]]
        .sort_values(["draft_year", "overall_pick", "name"], na_position="last")
        .head(80)
    )

    matched_top_pick_examples = (
        merged[
            merged["has_ncaa_match"]
            & pd.to_numeric(merged["overall_pick"], errors="coerce").between(1, 30)
        ][[
            "name", "draft_year", "overall_pick", "organization", "ncaa_source", "ncaa_player_raw",
            "ncaa_match_method", "ncaa_team", "ncaa_conf", "ncaa_games", "ncaa_ppg", "ncaa_rpg", "ncaa_apg",
            "ncaa_bpm", "ncaa_usage"
        ]]
        .sort_values(["draft_year", "overall_pick", "name"])
        .head(80)
    )

    unmatched_top_pick_examples = (
        merged[
            ~merged["has_ncaa_match"]
            & pd.to_numeric(merged["overall_pick"], errors="coerce").between(1, 30)
        ][[
            "name", "draft_year", "overall_pick", "draft_group_preview", "organization",
            "organization_type", "position"
        ]]
        .sort_values(["draft_year", "overall_pick", "name"])
        .head(80)
    )

    matched_2026_examples = (
        merged[merged["draft_year"].eq(2026) & merged["has_ncaa_match"]]
        [[
            "name", "draft_year", "overall_pick", "position", "ncaa_source", "ncaa_player_raw",
            "ncaa_match_method", "ncaa_team", "ncaa_conf", "ncaa_ppg", "ncaa_rpg", "ncaa_apg", "ncaa_bpm", "ncaa_usage"
        ]]
        .sort_values(["name"])
        .head(80)
    )

    unmatched_2026_examples = (
        merged[merged["draft_year"].eq(2026) & ~merged["has_ncaa_match"]]
        [["name", "draft_year", "overall_pick", "position", "organization", "organization_type"]]
        .sort_values(["name"])
        .head(80)
    )

    lines = []
    lines.append("# NBA Draft/Combine to Unified NCAA Merge Diagnostic Report")
    lines.append("")
    lines.append("This is a diagnostic report only. No merged CSV was saved.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(summary.to_markdown(index=False))
    lines.append("")

    lines.append("## Match Rate By draft_year")
    lines.append("")
    lines.append(safe_to_markdown(by_year))
    lines.append("")

    lines.append("## Match Rate By organization_type")
    lines.append("")
    lines.append(safe_to_markdown(by_org_type))
    lines.append("")

    lines.append("## Match Rate By draft_group_preview")
    lines.append("")
    lines.append(safe_to_markdown(by_group))
    lines.append("")

    lines.append("## Match Counts By ncaa_match_method")
    lines.append("")
    lines.append(safe_to_markdown(by_method))
    lines.append("")

    lines.append("## Manual Alias Player Status")
    lines.append("")
    lines.append(safe_to_markdown(manual_alias_status))
    lines.append("")

    lines.append("## Match Rate By draft_year And organization_type")
    lines.append("")
    lines.append(safe_to_markdown(by_year_org_type))
    lines.append("")

    lines.append("## Missing-Value Percentage For NCAA Columns After Left Join")
    lines.append("")
    lines.append(safe_to_markdown(ncaa_missing))
    lines.append("")

    lines.append("## Matched First-Round Examples")
    lines.append("")
    lines.append(safe_to_markdown(matched_top_pick_examples))
    lines.append("")

    lines.append("## Unmatched First-Round Examples")
    lines.append("")
    lines.append(safe_to_markdown(unmatched_top_pick_examples))
    lines.append("")

    lines.append("## Unmatched College/University Examples")
    lines.append("")
    lines.append(safe_to_markdown(unmatched_college_examples))
    lines.append("")

    lines.append("## Fuzzy Name Candidates For Unmatched College/University Examples")
    lines.append("")
    lines.append(safe_to_markdown(fuzzy_candidates))
    lines.append("")

    lines.append("## Matched 2026 Prediction-Pool Examples")
    lines.append("")
    lines.append(safe_to_markdown(matched_2026_examples))
    lines.append("")

    lines.append("## Unmatched 2026 Prediction-Pool Examples")
    lines.append("")
    lines.append(safe_to_markdown(unmatched_2026_examples))
    lines.append("")

    report_path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="data/nba_draft_combine_clean_2000_2026.csv")
    parser.add_argument("--ncaa", default="data/pre_draft_ncaa_unified_2000_2026.csv")
    parser.add_argument("--report", default="data/nba_draft_ncaa_merge_report.md")
    parser.add_argument("--fuzzy-limit", type=int, default=80)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    base_path = Path(args.base)
    ncaa_path = Path(args.ncaa)
    report_path = Path(args.report)

    base = pd.read_csv(base_path)
    ncaa = pd.read_csv(ncaa_path)

    for df_name, df in [("base", base), ("ncaa", ncaa)]:
        missing = set(KEY_COLS) - set(df.columns)
        if missing:
            raise ValueError(f"{df_name} is missing key columns: {sorted(missing)}")
        df["name"] = df["name"].map(clean_name)
        df["draft_year"] = pd.to_numeric(df["draft_year"], errors="coerce").astype("Int64")

    if "overall_pick" not in base.columns:
        raise ValueError("base dataset must contain overall_pick")
    if "organization_type" not in base.columns:
        raise ValueError("base dataset must contain organization_type")

    base = add_pick_group(base)
    base = add_name_keys(base)
    base = add_manual_alias_key(base)
    ncaa = add_name_keys(ncaa)

    merged, match_counts = diagnostic_left_join(base, ncaa)

    unmatched_college = merged[
        merged["organization_type"].eq("College/University")
        & ~merged["has_ncaa_match"]
    ].copy()
    fuzzy_candidates = make_fuzzy_candidates(unmatched_college, ncaa, limit=args.fuzzy_limit)

    write_report(base, ncaa, merged, fuzzy_candidates, report_path, match_counts)

    print(f"Saved merge diagnostic report: {report_path}")
    print(f"Base rows: {len(base)}")
    print(f"Merged rows for report: {len(merged)}")
    print(f"NCAA matches: {int(merged['has_ncaa_match'].sum())} / {len(merged)}")
    print(f"Exact-name matches: {match_counts['exact_name_matches']}")
    print(
        "Alternate-key matches: "
        f"{match_counts['compact_initials_matches'] + match_counts['spaced_initials_matches']}"
    )
    print(f"Manual alias matches: {match_counts['manual_alias_matches']}")
    college = merged[merged["organization_type"].eq("College/University")]
    if len(college):
        print(f"College/University matches: {int(college['has_ncaa_match'].sum())} / {len(college)}")


if __name__ == "__main__":
    main()
