#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".       

with open("./input/Names/invited_names.txt") as names:
    name_f = names.readlines()

with open("./input/Letters/starting_letter.txt") as letters:
    letter = letters.read()
    for name in name_f:
        new_letter = letter.replace("[name]", name.strip())
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as invite:
            invite.write(new_letter)