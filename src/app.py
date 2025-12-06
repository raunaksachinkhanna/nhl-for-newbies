from onboarding import user_inquiry # asking user what they want from the app 
from explanations import explain_game # explains game in simple and clean sentences
from data_loader import load_demo_game # load a single demo game's features from data/demo_games.csv.


def main() -> None:
    # 1) Ask the user what they're here for
    choice = user_inquiry()

    # 2) For now, always use the same demo game
    game_features = load_demo_game()

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
