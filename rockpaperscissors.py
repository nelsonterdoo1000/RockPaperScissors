# We import the random module that we will use to simulate the computers' choice in the game.
import random
# The line below requests an input from the user (The game player)
user_action = input("Enter a choice (R = rock, P = paper, S = scissors): \n")
# This specifies a list of the possible choices available to the user in the game
possible_actions = ["R", "P", "S"]
# This lines invokes the random module we had earlier imported that randomizes the computers'
#  choices in the game.
computer_action = random.choice(possible_actions)


def the_game():
    # This line prints put both the users choice and also that of the computer
    print(f"\nPlayer {user_action} : CPU {computer_action}.\n")
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "R":
        if computer_action == "S":
            #print("OOPPSS!! TRY AGAIN NEXT TIME")
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "P":
        if computer_action == "R":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "S":
        if computer_action == "P":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")


# this block checks if the user choice is not within the
# specified choice list and it keeps looping until the user enters the right choice
while True:
    user_action = input()
    if user_action not in possible_actions:
        print("Wrong input please, enter another choice")
        continue
    else:
        break


# This invokes the the_game function
the_game()
