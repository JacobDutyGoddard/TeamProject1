# All the functions used from gameLib are documented in that file, it imports library functions
import lib
# Random to generate our number
import random

def main():
    # AUTHOR: Jacob Duty
    # Main accepts no arguments
    # It will be the primary function that controls the game
    # It will gather the players playing the game, and then let the user change the number range, then play the game
    game_looping = "true"

    game_looping = display_menu()
    while game_looping == "true":
        game_player1, game_player2 = gatherPlayers()
        game_minimum, game_maximum = setRangeOfNumbers()

        winner = game(game_player1, game_player2, game_minimum, game_maximum)
        print(f"Congratulations {winner}!")

        game_looping = display_menu()


def display_menu():
    # AUTHOR: Jacob Duty
    # This function accepts no arguments
    # It will give the user a list of options to take them to different parts of the game
    # It will take the users input and then validate it, then run the function relevant to the input
    # It will return nothing
    print("1> Start a new game")
    print("2> Exit")
    choice = lib.gatherNumberInput("\n>")

    if(choice == 1):
        return "true"
    else:
        print("Thank you for playing Aizen and Jacob's awesome game!")
        return "false"

def gatherPlayers():
    # AUTHOR: Aizen Cannon
    # This function accepts any arguments
    # It will prompt the user for 2 string inputs
    # It will set the game_player1 to the first string, and then game_player2 to the second string
    # It will return nothing
    return lib.gatherStringInput("Please enter your first players name: "), lib.gatherStringInput("Please enter your second players name: ")

def setRangeOfNumbers():
    # AUTHOR: Aizen Cannon
    # This function accepts no arguments
    # It will get 2 users inputs, a minimum and maximum number (USE gameLib.gatherNumberInput())
    # Verify to make sure the second number is not smaller
    # Change game_minimum to the first input, change game_maximum to the second input
    min_number = lib.gatherNumberInput("Input the minimum number: ")
    max_number = lib.gatherNumberInput("Input the maximum number: ")

    if(max_number > min_number):
        return min_number, max_number
    else:
        return max_number, min_number

def game(player1, player2, MIN, MAX):
    # AUTHOR: Jacob Duty, Aizen Cannon
    # This function accepts 4 arguments, player1, player2, MIN, MAX
    # It will create a random number and then loop until its guessed correctly
    # It will provide feedback and then return who won
    correct_num = random.randint(MIN, MAX)
    guess = -50

    while guess != correct_num:
        print(f"{player1}'s turn!")
        guess = lib.gatherNumberInput(f"{MIN}-{MAX} |> ")

        if guess == correct_num:
            return player1
        elif guess > correct_num:
            MAX = min(guess, MAX)
            print("Too high!")
        elif guess < correct_num:
            MIN = max(guess, MIN)
            print("Too low!")

        print(f"{player2}'s turn!")
        guess = lib.gatherNumberInput(f"{MIN}-{MAX} |> ")
        
        if guess == correct_num:
            return player2
        elif guess > correct_num:
            MAX = min(guess, MAX)
            print("Too high!")
        elif guess < correct_num:
            MIN = max(guess, MIN)
            print("Too low!")

main()