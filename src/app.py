from onboarding import user_inquiry # asking user what they want from the app 
from explanations import explain_game # explains game in simple and clean sentences

def get_demo_game_features() -> dict:
    """
    Temporary helper: returns hard-coded features for one demo game.
    Later this will be replaced with real data from a CSV or API.
    """
    return {
        "home_team": "VAN",
        "away_team": "CGY",
        "home_goals_for_last5": 3.8,
        "away_goals_for_last5": 2.1,
        "league_avg_goals_for_last5": 3.0,
        "home_rest_days": 2,
        "away_rest_days": 0,
    }

def main() -> None:
    # 1) Ask the user what they're here for
    choice = user_inquiry()

    # 2) For now, always use the same demo game
    game_features = get_demo_game_features()

    print(f"\nSelected game: {game_features['home_team']} vs {game_features['away_team']}")

    if choice == "1":
        # Quick prediction mode – model not built yet
        print("\n[Quick prediction mode]")
        print("Model coming soon: this will show a win probability like 'VAN 62% – 38% CGY'.")
    elif choice == "2":
        # Understand why – use the explanation engine
        print("\n[Understand why mode]")
        print("Here are some key reasons this matchup looks the way it does:")
        for line in explain_game(game_features):
            print("•", line)
    else:
        # Learn something – reuse explanations, but highlight the teaching angle
        print("\n[Learn something mode]")
        print("Let's use this game to learn a couple of concepts:")
        for line in explain_game(game_features):
            print("•", line)
        print(
            "\nSoon this mode will add short explanations of concepts like 'rest days', "
            "'recent form', or 'hot goalie' in very simple terms."
        )

if __name__ == "__main__":
    main()
