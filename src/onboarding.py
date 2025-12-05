def user_inquiry() -> str:
    #welcomes user to the app
    print("Welcome to nhl-for-newbies! 🏒")
    #mini introduction
    print("Making NHL games make sense, minus the scary advanced stats 🥶\n")
    #asks the user for the 3 choices
    print(
        "1) Quick prediction (bro just tell me who's gonna win)\n"
        "2) Understand why (bro just explain it in simple language)\n"
        "3) Learn something (teach me some concepts using a game)"
    )
    #user enters a choice and the system returns a selected mode
    while True:
        choice = input("Type 1, 2, or 3 and press Enter: \n").strip()
        if choice in {"1", "2", "3"}:
            return choice
        print("Please type 1, 2, or 3.")

def main() -> None:
    choice = user_inquiry()

    if choice == "1":
        print("\nMode selected: Quick prediction.")
    elif choice == "2":
        print("\nMode selected: Understand why.")
    else:
        print("\nMode selected: Learn something.")

if __name__ == "__main__":
    main()