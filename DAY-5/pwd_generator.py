import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))


pwd = []
shuf1 = random.sample(letters, len(letters))
shuf2 = random.sample(numbers, len(numbers))
shuf3 = random.sample(symbols, len(symbols))

for i in range(0, nr_letters):
    pwd += shuf1[i]

for i in range(0, nr_symbols):
    pwd += shuf3[i]

for i in range(0, nr_numbers):
    pwd += shuf2[i]

print("".join(pwd))

ans = random.sample(pwd, len(pwd))

password = "".join(ans)
print(f"Your password is {password}")


# Angela's solution
password_list = []
for i in range(0, nr_letters):
    password_list += random.choice(letters)

for i in range(0, nr_symbols):
    password_list += random.choice(symbols)

for i in range(0, nr_numbers):
    password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is {password}")
