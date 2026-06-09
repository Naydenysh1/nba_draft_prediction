#!/usr/bin/env python3
"""
Build the static JSON payload for the 2026 NBA Draft dashboard.

The script does not retrain or rewrite model outputs. It reads saved CSV files
from data/final, computes agreement/evaluation summaries, and writes
docs/data/dashboard.json for the GitHub Pages frontend.
"""

from __future__ import annotations

import json
import re
import string
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
FINAL_DIR = ROOT / "data" / "final"
EXTERNAL_DIR = ROOT / "data" / "external"
DOCS_DATA_DIR = ROOT / "docs" / "data"

MODEL_BOARD_PATH = FINAL_DIR / "final_2026_model_draft_board.csv"
COMPARISON_PATH = FINAL_DIR / "comparison_2026_model_vs_espn.csv"
ESPN_FINAL_PATH = FINAL_DIR / "espn_mock_draft_2026.csv"
ESPN_EXTERNAL_PATH = EXTERNAL_DIR / "espn_mock_draft_2026.csv"
ACTUAL_PATH = FINAL_DIR / "actual_draft_2026.csv"
OUTPUT_PATH = DOCS_DATA_DIR / "dashboard.json"

GROUP_ORDER = ["top_5", "picks_6_14", "picks_15_30", "second_round", "undrafted"]
GROUP_LABELS = {
    "top_5": "Top 5",
    "picks_6_14": "Picks 6-14",
    "picks_15_30": "Picks 15-30",
    "second_round": "Second round",
    "undrafted": "Undrafted",
}
GROUP_INDEX = {group: idx for idx, group in enumerate(GROUP_ORDER)}

NAME_ALIASES = {
    "aj dybantsa": "anicet dybantsa",
    "nate ament": "nathaniel ament",
    "matt able": "matthew able",
    "chris cenac": "christopher cenac",
    "mikel brown": "christopher brown",
}


def normalize_name(value: object) -> str:
    """Normalize names for joining model, ESPN, and future actual data."""
    if pd.isna(value):
        return ""
    text = str(value).lower().strip()
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = re.sub(r"\([^)]*\)", " ", text)
    text = text.translate(str.maketrans({ch: " " for ch in string.punctuation}))
    text = re.sub(r"\b(jr|sr|ii|iii|iv|v)\b", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return NAME_ALIASES.get(text, text)


def read_csv(path: Path, required: bool = True) -> pd.DataFrame:
    if not path.exists():
        if required:
            raise FileNotFoundError(f"Required input not found: {path.relative_to(ROOT)}")
        return pd.DataFrame()
    return pd.read_csv(path)


def clean_group(value: object) -> str:
    if pd.isna(value):
        return "undrafted"
    text = str(value).strip()
    return text if text in GROUP_INDEX else text


def pick_to_group(value: object) -> str:
    pick = pd.to_numeric(pd.Series([value]), errors="coerce").iloc[0]
    if pd.isna(pick) or int(pick) == 999:
        return "undrafted"
    pick = int(pick)
    if 1 <= pick <= 5:
        return "top_5"
    if 6 <= pick <= 14:
        return "picks_6_14"
    if 15 <= pick <= 30:
        return "picks_15_30"
    if 31 <= pick <= 60:
        return "second_round"
    return "undrafted"


def group_counts(df: pd.DataFrame, col: str) -> list[dict[str, Any]]:
    counts = df[col].value_counts(dropna=False).to_dict() if col in df else {}
    return [
        {"group": group, "label": GROUP_LABELS[group], "count": int(counts.get(group, 0))}
        for group in GROUP_ORDER
    ]


def confusion_matrix(df: pd.DataFrame, row_col: str, col_col: str) -> dict[str, Any]:
    matrix = []
    for row_group in GROUP_ORDER:
        row = []
        for col_group in GROUP_ORDER:
            count = int(((df[row_col] == row_group) & (df[col_col] == col_group)).sum())
            row.append(count)
        matrix.append(row)
    return {
        "row_label": row_col,
        "column_label": col_col,
        "groups": [{"key": group, "label": GROUP_LABELS[group]} for group in GROUP_ORDER],
        "matrix": matrix,
    }


def classification_metrics(df: pd.DataFrame, pred_col: str, actual_col: str) -> dict[str, Any]:
    eval_df = df[df[pred_col].notna() & df[actual_col].notna()].copy()
    n = int(len(eval_df))
    exact = int((eval_df[pred_col] == eval_df[actual_col]).sum()) if n else 0
    adjacent = int(
        eval_df.apply(
            lambda row: abs(GROUP_INDEX.get(row[pred_col], 99) - GROUP_INDEX.get(row[actual_col], -99)) <= 1,
            axis=1,
        ).sum()
    ) if n else 0

    report = []
    for group in GROUP_ORDER:
        tp = int(((eval_df[pred_col] == group) & (eval_df[actual_col] == group)).sum())
        fp = int(((eval_df[pred_col] == group) & (eval_df[actual_col] != group)).sum())
        fn = int(((eval_df[pred_col] != group) & (eval_df[actual_col] == group)).sum())
        support = int((eval_df[actual_col] == group).sum())
        precision = tp / (tp + fp) if (tp + fp) else 0.0
        recall = tp / (tp + fn) if (tp + fn) else 0.0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else 0.0
        report.append(
            {
                "group": group,
                "label": GROUP_LABELS[group],
                "precision": round(precision, 4),
                "recall": round(recall, 4),
                "f1": round(f1, 4),
                "support": support,
            }
        )

    return {
        "n": n,
        "exact_matches": exact,
        "accuracy": round(exact / n, 4) if n else None,
        "adjacent_or_exact_matches": adjacent,
        "adjacent_or_exact_rate": round(adjacent / n, 4) if n else None,
        "classification_report": report,
    }


def disagreement_score(row: pd.Series, left_col: str, right_col: str) -> int:
    return abs(GROUP_INDEX.get(row[left_col], 99) - GROUP_INDEX.get(row[right_col], 99))


def select_model_group(board: pd.DataFrame) -> pd.Series:
    if "model_group" in board:
        return board["model_group"]
    if "ranked_model_group" in board:
        return board["ranked_model_group"]
    if "predicted_group" in board:
        return board["predicted_group"]
    raise ValueError("Model board must contain model_group, ranked_model_group, or predicted_group.")


def records(df: pd.DataFrame, columns: list[str], limit: int | None = None) -> list[dict[str, Any]]:
    existing = [col for col in columns if col in df.columns]
    out = df[existing].copy()
    if limit is not None:
        out = out.head(limit)
    out = out.where(pd.notna(out), None)
    return out.to_dict(orient="records")


def prepare_inputs() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    board = read_csv(MODEL_BOARD_PATH)
    comparison = read_csv(COMPARISON_PATH)
    espn_path = ESPN_FINAL_PATH if ESPN_FINAL_PATH.exists() else ESPN_EXTERNAL_PATH
    espn = read_csv(espn_path)

    for frame in (board, comparison, espn):
        if "name" not in frame:
            raise ValueError("All dashboard inputs must contain a name column.")
        frame["name_normalized"] = frame["name"].map(normalize_name)

    board["model_group"] = select_model_group(board).map(clean_group)
    comparison["model_group"] = comparison["model_group"].map(clean_group)
    comparison["espn_group"] = comparison["espn_group"].map(clean_group)

    if "espn_group" not in espn:
        if "mock_group" in espn:
            espn["espn_group"] = espn["mock_group"]
        else:
            espn["espn_group"] = espn["mock_pick"].map(pick_to_group)
    espn["espn_group"] = espn["espn_group"].map(clean_group)
    return board, comparison, espn


def build_pre_draft(board: pd.DataFrame, comparison: pd.DataFrame, espn: pd.DataFrame) -> dict[str, Any]:
    model_names = set(board["name_normalized"])
    main = comparison[comparison["name_normalized"].isin(model_names)].copy()
    main["agreement"] = main["model_group"] == main["espn_group"]
    main["gap"] = main.apply(disagreement_score, left_col="model_group", right_col="espn_group", axis=1)

    espn_only = espn[~espn["name_normalized"].isin(model_names)].copy()

    metrics = classification_metrics(main, "model_group", "espn_group")
    return {
        "mode": "pre_draft_agreement",
        "mode_label": "Pre-draft agreement mode",
        "note": "ESPN mock draft data is not ground truth. This dashboard is an agreement analysis until actual 2026 draft results are added.",
        "agreement": metrics,
        "distributions": {
            "model": group_counts(main, "model_group"),
            "espn": group_counts(main, "espn_group"),
        },
        "confusion_matrices": {
            "model_vs_espn": confusion_matrix(main, "model_group", "espn_group"),
        },
        "largest_disagreements": records(
            main.sort_values(["gap", "name"], ascending=[False, True]),
            ["name", "model_group", "espn_group", "gap"],
            limit=5,
        ),
        "espn_only_outside_model_pool": records(
            espn_only.sort_values("mock_pick") if "mock_pick" in espn_only else espn_only,
            ["mock_pick", "name", "position", "organization", "espn_group"],
            limit=25,
        ),
        "comparison_rows": records(main.sort_values(["model_group", "name"]), ["name", "model_group", "espn_group"]),
    }


def build_post_draft(board: pd.DataFrame, comparison: pd.DataFrame, espn: pd.DataFrame) -> dict[str, Any]:
    actual = read_csv(ACTUAL_PATH)
    if "name" not in actual or "overall_pick" not in actual:
        raise ValueError("actual_draft_2026.csv must contain name and overall_pick columns.")
    actual["name_normalized"] = actual["name"].map(normalize_name)
    actual["actual_group"] = actual["overall_pick"].map(pick_to_group)

    model = board[["name", "name_normalized", "model_group"]].copy()
    model = model.drop_duplicates("name_normalized", keep="first")
    espn_cols = ["name", "name_normalized", "espn_group"]
    if "mock_pick" in espn:
        espn_cols.insert(2, "mock_pick")
    espn_side = espn[espn_cols].drop_duplicates("name_normalized", keep="first")

    merged = model.merge(
        espn_side.rename(columns={"name": "espn_name"}),
        on="name_normalized",
        how="outer",
    )
    merged = merged.merge(
        actual[["name", "name_normalized", "overall_pick", "actual_group"]].rename(columns={"name": "actual_name"}),
        on="name_normalized",
        how="left",
    )
    merged["actual_group"] = merged["actual_group"].fillna("undrafted")
    merged["display_name"] = merged["actual_name"].combine_first(merged["name"]).combine_first(merged["espn_name"])
    merged["model_espn_gap"] = merged.apply(
        lambda row: disagreement_score(row, "model_group", "espn_group")
        if pd.notna(row.get("model_group")) and pd.notna(row.get("espn_group"))
        else None,
        axis=1,
    )

    model_eval = merged[merged["model_group"].notna()].copy()
    espn_eval = merged[merged["espn_group"].notna()].copy()
    model_espn = merged[merged["model_group"].notna() & merged["espn_group"].notna()].copy()

    return {
        "mode": "post_draft_evaluation",
        "mode_label": "Post-draft evaluation mode",
        "note": "Actual 2026 draft results are present, so model and ESPN predictions are evaluated against actual draft groups.",
        "model_vs_actual": classification_metrics(model_eval, "model_group", "actual_group"),
        "espn_vs_actual": classification_metrics(espn_eval, "espn_group", "actual_group"),
        "model_vs_espn": classification_metrics(model_espn, "model_group", "espn_group"),
        "distributions": {
            "actual": group_counts(merged, "actual_group"),
            "model": group_counts(model_eval, "model_group"),
            "espn": group_counts(espn_eval, "espn_group"),
        },
        "confusion_matrices": {
            "model_vs_actual": confusion_matrix(model_eval, "model_group", "actual_group"),
            "espn_vs_actual": confusion_matrix(espn_eval, "espn_group", "actual_group"),
            "model_vs_espn": confusion_matrix(model_espn, "model_group", "espn_group"),
        },
        "three_way_comparison": records(
            merged.sort_values(["overall_pick", "display_name"], na_position="last"),
            ["display_name", "overall_pick", "actual_group", "model_group", "espn_group", "mock_pick"],
        ),
        "largest_disagreements": records(
            model_espn.sort_values(["model_espn_gap", "display_name"], ascending=[False, True]),
            ["display_name", "model_group", "espn_group", "model_espn_gap"],
            limit=5,
        ),
    }


def build_payload() -> dict[str, Any]:
    board, comparison, espn = prepare_inputs()
    mode_payload = build_post_draft(board, comparison, espn) if ACTUAL_PATH.exists() else build_pre_draft(board, comparison, espn)
    espn_source_path = ESPN_FINAL_PATH if ESPN_FINAL_PATH.exists() else ESPN_EXTERNAL_PATH

    comparison_groups = comparison[["name_normalized", "espn_group"]].drop_duplicates("name_normalized", keep="first")
    board_display = board.merge(comparison_groups, on="name_normalized", how="left")
    board_sort = board_display.sort_values("model_rank") if "model_rank" in board_display else board_display.copy()
    board_columns = [
        "model_rank",
        "name",
        "position",
        "organization",
        "model_group",
        "espn_group",
        "draft_board_score",
        "max_probability",
        "prob_top_5",
        "prob_picks_6_14",
        "prob_picks_15_30",
        "prob_second_round",
        "prob_undrafted",
    ]

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "project_title": "2026 NBA Draft Prediction Dashboard",
        "summary": "Static dashboard for saved 2026 NBA Draft model predictions, ESPN mock-draft agreement, and future actual draft evaluation.",
        "groups": [{"key": group, "label": GROUP_LABELS[group]} for group in GROUP_ORDER],
        "source_files": {
            "model_board": MODEL_BOARD_PATH.relative_to(ROOT).as_posix(),
            "comparison": COMPARISON_PATH.relative_to(ROOT).as_posix(),
            "espn_mock": espn_source_path.relative_to(ROOT).as_posix(),
            "actual_draft": ACTUAL_PATH.relative_to(ROOT).as_posix() if ACTUAL_PATH.exists() else None,
        },
        "top_model_board": records(board_sort, board_columns, limit=60),
        **mode_payload,
    }


def main() -> None:
    payload = build_payload()
    DOCS_DATA_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH.relative_to(ROOT)}")
    print(f"Mode: {payload['mode_label']}")


if __name__ == "__main__":
    main()
