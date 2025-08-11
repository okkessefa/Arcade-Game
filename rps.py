import random
from enum import Enum

def rps(name="Player 1"):
    game_count = 0
    player_count = 0
    python_count = 0

    def rps_game():
        nonlocal name
        nonlocal game_count

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(
            f"\n{name}, please enter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, you must enter 1, 2, or 3.")
            return rps_game()

        player = int(playerchoice)

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print(
            f"\n{name}, you choose {str(RPS(player)).replace('RPS.', '').title()}."
        )
        print(
            f"Python choose {str(RPS(computer)).replace('RPS.', '').title()}.\n"
        )

        def decide_winner():
            nonlocal name
            nonlocal player_count
            nonlocal python_count

            if player == 1 and computer == 3:
                player_count +=1
                return f"{name}, you win!🎉"
            
            elif player == 2 and computer == 1:
                player_count +=1
                return f"{name}, you win!🎉"
            
            elif player == 3 and computer == 2:
                player_count +=1
                return f"{name}, you win!🎉"
            
            elif player == computer:
                return "😲 Tie game!"
            
            else:
                python_count += 1
                return f"🐍 Python wins!\n Sorry {name}..."

        game_result = decide_winner()

        print(game_result)
        game_count += 1
        print("--------------------------------------------------------")
        print(
            f"\n Game count: { game_count }"
        )
        print(
            f"\n {name} count: { player_count }"
        )
        print(
            f"\n Python count: { python_count}"
        )
        print(
            f"\n Tie count: { game_count - (player_count + python_count ) }"
        )
        print("--------------------------------------------------------")


        print("\nPlay again?")

        while True:
            playagain = input("\nY for Yes or \nQ to Quit \n\n")

            if playagain.capitalize() not in ["Y", "Q"]:
                continue
            else:
                break

        if playagain.capitalize() == "Y":
            return rps_game()

        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")

    rps_game()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person to playing the game."
    )

    args = parser.parse_args()

    play = rps(args.name) 
    play()