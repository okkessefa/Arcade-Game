import random

def guess(name="Player 1"):
    game_count = 0

    def guess_game():
        nonlocal name
        nonlocal game_count

        player_choice = int(input(
            f"{name}, please enter one of these number: 1, 2, 3"
        ))
        print(f"{name}, good luck")
        if player_choice not in {1,2,3}:
            print(f"{name}, you must enter 1, 2, or 3 ")
            return guess_game
        
        computer_choice = random.randint(1,3)

        print(
            f"\n{name}, you chooses {player_choice}"
            )

        def win_decider():
            nonlocal name

            if player_choice == computer_choice:
                return f"\nI was thinking {computer_choice}.\n{name}, good shot ✅"
            else:
                return f"\nThe number was {computer_choice}.\n{name}, nice try ❌"

        game_result = win_decider()

        print(game_result)

        print("Play again?")

        while(True):
            play_again = input("\nY for Yes or \n Q to Quit \n\n")
            

            if play_again.capitalize() not in ["Y", "Q"]:
                continue
            else:
                break

        if play_again.capitalize() == "Y":
            return guess_game()

        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")

    guess_game()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience"
    )

    parser.add_argument(
        "-n","--name", metavar="name",
        required=True, help="The name of the person to play the game"
    )
    args = parser.parse_args()

    play_guess = guess(args.name)
    play_guess()