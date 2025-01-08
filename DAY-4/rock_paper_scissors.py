import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
gameImages = [rock, paper, scissors]
personalChoice = int(
    input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors. \n")
)
if personalChoice >= 0 and personalChoice <= 2:
    print(gameImages[personalChoice])

computerChoice = random.randint(0, 2)
print("Computer chose:")
print(gameImages[computerChoice])

if personalChoice >= 3 or personalChoice < 0:
    print("You typed an invalid number, you loose!")
elif personalChoice == 0 and computerChoice == 2:
    print("You win")
elif computerChoice == 0 and personalChoice == 2:
    print("You lose")
elif personalChoice == computerChoice:
    print("It's a draw")
elif personalChoice > computerChoice:
    print("You win")
elif computerChoice > personalChoice:
    print("You lose")
