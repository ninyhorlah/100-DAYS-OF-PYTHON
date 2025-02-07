import random
from game_data import data
from art import logo, vs

"""
* pick 2 dict at random and compare
* if comparison is right, record score
* if right, move the highest to the top and compare with another
* if wrong, end the game and calculate total score
"""

"""
* pick 2 dict at random and compare
- use random with range
"""

game_data = data

score = 0

print(logo)
celeb1 = random.choice(game_data)
celeb2 = random.choice(game_data)


def check():
    print(f"Compare A: {celeb1['name']}, {celeb1['description']}, {celeb1['country']}")
    print(vs)
    print(f"Against B: {celeb2['name']}, {celeb2['description']}, {celeb2['country']}")


check()

should_continue = True
while should_continue:
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n" * 20)
    print(logo)

    def right():
        print(f"You're right! Current score: {score}")

    if user_choice == "a" and celeb1["follower_count"] > celeb2["follower_count"]:
        score += 1
        right()
        celeb1 = celeb1
        celeb2 = random.choice(game_data)
        check()
    elif user_choice == "b" and celeb2["follower_count"] > celeb1["follower_count"]:
        score += 1
        right()
        celeb1 = celeb2
        celeb2 = random.choice(game_data)
        check()
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        should_continue = False
