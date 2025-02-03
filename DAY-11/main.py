# import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    card = random.choice(cards)
    return card


deal_card()

user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    # print(user_cards)


def calculate_score(cards):
    if cards == 21 and len(cards) == 2:
        return 0
    if 11 in cards and cards > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


calculate_score(user_cards)
