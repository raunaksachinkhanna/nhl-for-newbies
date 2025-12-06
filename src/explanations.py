def explain_game(game_features: dict) -> list[str]:
    """
    Turn simple numeric features about a game into plain-English sentences.
    For now we only look at recent scoring and rest days.
    """
    sentences: list[str] = []

    home = game_features["home_team"]
    away = game_features["away_team"]

    # 1) Recent offence (goals per game over last 5)
    home_diff = game_features["home_goals_for_last5"] - game_features["league_avg_goals_for_last5"]
    away_diff = game_features["away_goals_for_last5"] - game_features["league_avg_goals_for_last5"]

    if home_diff >= 0.8:
        sentences.append(f"{home}'s offence has been hot in the last 5 games.")
    elif home_diff <= -0.8:
        sentences.append(f"{home} has struggled to score in the last 5 games.")

    if away_diff >= 0.8:
        sentences.append(f"{away}'s offence has been hot in the last 5 games.")
    elif away_diff <= -0.8:
        sentences.append(f"{away} has struggled to score in the last 5 games.")

    # 2) Rest days (back-to-back vs rested)
    home_rest = game_features["home_rest_days"]
    away_rest = game_features["away_rest_days"]

    if home_rest == 0 and away_rest >= 1:
        sentences.append(f"{home} is on a back-to-back, so they may be more tired than {away}.")
    elif away_rest == 0 and home_rest >= 1:
        sentences.append(f"{away} is on a back-to-back, so they may be more tired than {home}.")
    elif home_rest >= 2 and away_rest <= 1:
        sentences.append(f"{home} is a bit more rested coming into this game.")
    elif away_rest >= 2 and home_rest <= 1:
        sentences.append(f"{away} is a bit more rested coming into this game.")

    if not sentences:
        sentences.append("Nothing too extreme here — both teams look pretty normal on form and rest.")

    return sentences

def main() -> None:
    # TEMP: one hard-coded game; later this will come from real data
    game_features = {
        "home_team": "VAN",
        "away_team": "CGY",
        "home_goals_for_last5": 3.8,
        "away_goals_for_last5": 2.1,
        "league_avg_goals_for_last5": 3.0,
        "home_rest_days": 2,
        "away_rest_days": 0,
    }

    print(f"Explanation for {game_features['home_team']} vs {game_features['away_team']}:")
    for line in explain_game(game_features):
        print("•", line)

if __name__ == "__main__":
    main()
