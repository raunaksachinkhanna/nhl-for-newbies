# src/data_loader.py

import csv
from pathlib import Path
from typing import Dict


def load_demo_game() -> Dict[str, object]:
    """
    Load a single demo game's features from data/demo_games.csv.

    For now this just returns the first row as a dict with the exact keys that
    explain_game() expects.
    """
    data_path = Path(__file__).resolve().parent.parent / "data" / "demo_games.csv"

    with data_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        row = next(reader)  # first (and only) row for now

    # Convert numeric fields from strings to proper types
    return {
        "home_team": row["home_team"],
        "away_team": row["away_team"],
        "home_goals_for_last5": float(row["home_goals_for_last5"]),
        "away_goals_for_last5": float(row["away_goals_for_last5"]),
        "league_avg_goals_for_last5": float(row["league_avg_goals_for_last5"]),
        "home_rest_days": int(row["home_rest_days"]),
        "away_rest_days": int(row["away_rest_days"]),
    }
