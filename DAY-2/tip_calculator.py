print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))


tip = tip / 100 * bill
bill_n_tip = tip + bill
sharing = bill_n_tip / people

total = round(sharing, 2)
print(f"Each person should pay: {total}")
