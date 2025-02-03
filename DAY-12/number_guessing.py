import random
from art import logo

chosen_num = random.randint(1, 100)
should_continue = True

print(logo)
level_choice = input(
    "Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100. \nChoose a difficulty. Type 'easy' or 'hard': "
).lower()
decision = ""
no_of_lives = {"easy": 10, "hard": 2}


def guess(u_choice):
    if u_choice > chosen_num:
        print(
            f"You have {no_of_lives[level_choice]} attempts remaining to guess the number."
        )
        print("Too high.\nGuess again.")
    elif u_choice < chosen_num:
        print(
            f"You have {no_of_lives[level_choice]} attempts remaining to guess the number."
        )
        print("Too Low.\nGuess again.")
    else:
        print("You got it")


if level_choice == "hard" or level_choice == "easy":
    print(
        f"You have {no_of_lives[level_choice]} attempts remaining to guess the number."
    )
    decision = level_choice
else:
    print("Your input is not part of the option. Start again!")
    should_continue = False


def check_the_guess():
    user_choice = int(input("Make a guess: "))
    if no_of_lives[level_choice] != 0:
        guess(user_choice)
    else:
        print("You've run out of guesses. Refresh the page to run again.")


while should_continue:
    if no_of_lives[level_choice] == 0:
        should_continue = False
    elif no_of_lives[level_choice] > 0:
        no_of_lives[level_choice] -= 1
        check_the_guess()
    else:
        should_continue = False
