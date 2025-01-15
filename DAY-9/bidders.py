import art

print(art.logo)
# TODO-1: Ask the user for input
auction = {}
# TODO-2: Save data into dictionary {name: price}

# TODO-3: Whether if new bids need to be added
continue_bidding = True
while continue_bidding:
    name = input("What is your name? ")
    price = int(input("What is your bidding price? $"))
    auction[name] = price
    should_continue = input("Any other bidders? type 'yes' or 'no'").lower()
    if should_continue == "yes":
        print("\n" * 20)
    else:
        continue_bidding = False

# TODO-4: Compare bids in dictionary


def highest_bidder(highest_bid):
    high_bid = 0
    winner = ""
    for bidders in highest_bid:
        if highest_bid[bidders] > high_bid:
            high_bid = highest_bid[bidders]
            winner = bidders
    print(f"The winner is {winner} with a bid of ${high_bid}")


highest_bidder(auction)
