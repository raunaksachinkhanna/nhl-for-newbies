# src/features.py

from pathlib import Path
import csv
from typing import Dict, List


def load_raw_demo_row() -> Dict[str, object]:
    """
    Load the first (and currently only) raw demo game row from data/demo_games.csv.

    This returns the raw fields from the CSV as a dict, with numeric values cast
    to float/int where appropriate.
    """
    data_path = Path(__file__).resolve().parent.parent / "data" / "demo_games.csv"

    with data_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        row = next(reader)

    return {
        "home_team": row["home_team"],
        "away_team": row["away_team"],
        "home_goals_for_last5": float(row["home_goals_for_last5"]),
        "away_goals_for_last5": float(row["away_goals_for_last5"]),
        "league_avg_goals_for_last5": float(row["league_avg_goals_for_last5"]),
        "home_rest_days": int(row["home_rest_days"]),
        "away_rest_days": int(row["away_rest_days"]),
    }


def build_model_features(raw_row: Dict[str, object]) -> Dict[str, float]:
    """
    Given a raw game row, compute a minimal set of numeric features for the model.

    v1 feature set:
      - offence_diff: home_goals_for_last5 - away_goals_for_last5
      - rest_diff:    home_rest_days - away_rest_days
      - home_advantage: 1.0  (home team is at home)
    """
    home_goals = raw_row["home_goals_for_last5"]
    away_goals = raw_row["away_goals_for_last5"]
    home_rest = raw_row["home_rest_days"]
    away_rest = raw_row["away_rest_days"]

    offence_diff = float(home_goals) - float(away_goals)
    rest_diff = float(home_rest) - float(away_rest)
    home_advantage = 1.0  # always 1 for now; model learns weight of being at home

    return {
        "offence_diff": offence_diff,
        "rest_diff": rest_diff,
        "home_advantage": home_advantage,
    }


def demo_features() -> None:
    """
    Convenience function to print raw + model features for the demo game.
    Useful for sanity checking and for explaining the feature set in the README/PR.
    """
    raw = load_raw_demo_row()
    model_feats = build_model_features(raw)

    print("Raw demo row:")
    for k, v in raw.items():
        print(f"  {k}: {v}")

    print("\nDerived model features:")
    for k, v in model_feats.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    demo_features()
