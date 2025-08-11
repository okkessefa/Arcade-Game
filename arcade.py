import rps
import guess_number
import sys

def game_decider(name = "Player 1"):
    
    def arcade_game():
        nonlocal name
         
        print(f"{name}, welcome to arcade arena ")

        selected_game = input(
            f"{name}, please choose a game: \n 1 = Rock Paper Scsiccors \n 2= Guess My Number \n Or pres 'Q' to exit the Arcade\n"
            )

        def gameDecider():
            nonlocal name

            if selected_game == "1":
                return rps.rps(name)
            elif selected_game == "2":
                return guess_number.guess(name)
            elif selected_game == "Q" or selected_game == "q" :
                print("\n🎉🎉🎉🎉")
                print("Thank you for playing!\n")
                sys.exit()
            else:
                return arcade_game()
            
        gameDecider()
            
        print(f"Welcome back to Arcade Arena {name}")

        while(True):
            playAgain = input("\nY for Yes or Q for Quit\n\n")

            if playAgain.capitalize() not in ["Y", "Q"]:
                continue
            else:
                break
    
        if playAgain.capitalize() == "Y":
            return arcade_game()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            sys.exit(f"Bye! {name} 👋")
    
    arcade_game()

    
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person to greet."
    )

    args = parser.parse_args()
    play = game_decider(args.name)

    play()