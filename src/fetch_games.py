# src/fetch_games.py

from __future__ import annotations

import json
from datetime import date
from pathlib import Path
from typing import Any, Dict, List

import requests


BASE_URL = "https://api-web.nhle.com/v1"
RAW_DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"


def fetch_schedule_for_date(day: date) -> Dict[str, Any]:
    """
    Fetch the NHL schedule for a single date from the api-web.nhle.com API.
    Example URL: https://api-web.nhle.com/v1/schedule/2025-12-01
    """
    url = f"{BASE_URL}/schedule/{day.isoformat()}"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    return resp.json()


def save_raw_schedule(data: Dict[str, Any], label: str) -> Path:
    """
    Save the raw schedule JSON to data/raw as a pretty-printed file.
    """
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
    out_path = RAW_DATA_DIR / f"nhle_schedule_{label}.json"
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    return out_path


def extract_games(schedule_json: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Flatten the api-web.nhle.com schedule JSON into a simple list of games.

    Each game dict contains:
      - game_id
      - game_date
      - game_type
      - venue
      - home_team_abbrev / away_team_abbrev
      - home_team_name / away_team_name
      - home_score / away_score
    """
    games: List[Dict[str, Any]] = []

    for week in schedule_json.get("gameWeek", []):
        game_date = week.get("date")  # same for all games in that block
        for game in week.get("games", []):
            home = game.get("homeTeam", {}) or {}
            away = game.get("awayTeam", {}) or {}

            games.append(
                {
                    "game_id": game.get("id"),
                    "game_date": game_date,
                    "game_type": game.get("gameType"),
                    "venue": game.get("venue", {}).get("default", ""),
                    "home_team_abbrev": home.get("abbrev"),
                    "away_team_abbrev": away.get("abbrev"),
                    "home_team_name": home.get("name", ""),
                    "away_team_name": away.get("name", ""),
                    "home_score": game.get("homeTeamScore"),
                    "away_score": game.get("awayTeamScore"),
                }
            )

    return games


def save_flat_games(games: List[Dict[str, Any]], label: str) -> Path:
    """
    Save the flattened games list to data/raw as JSON.
    """
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
    out_path = RAW_DATA_DIR / f"nhle_games_flat_{label}.json"
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(games, f, indent=2)
    return out_path


def main() -> None:
    # For now, hard-code one date that we know works
    target = date(2025, 12, 1)

    print(f"Fetching NHL schedule for {target}...")
    schedule_json = fetch_schedule_for_date(target)
    print("Got response with top-level keys:", list(schedule_json.keys()))

    raw_path = save_raw_schedule(schedule_json, target.isoformat())
    print(f"Saved raw schedule JSON to: {raw_path}")

    games = extract_games(schedule_json)
    print(f"Extracted {len(games)} games from schedule JSON.")

    flat_path = save_flat_games(games, target.isoformat())
    print(f"Saved flattened games JSON to: {flat_path}")


if __name__ == "__main__":
    main()

