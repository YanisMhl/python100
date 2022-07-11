import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nLetters = int(input("How many letters would you like in your password?\n"))
nSymbols = int(input("How many symbols would you like?\n"))
nNumbers = int(input("How many numbers would you like?\n"))

password=""
randomChoice = 0
iterations = nLetters + nSymbols + nNumbers

while iterations > 0:
    randomChoice = random.randint(0, 2)
    if randomChoice == 0: #it means letter
        if nLetters > 0:
            password += letters[random.randint(0, len(letters)-1)]
            iterations -= 1
            nLetters -= 1
        else:
            randomChoice = random.randint(0, 2)
    if randomChoice == 1: #it means symbol
        if nSymbols > 0:
            password += symbols[random.randint(0, len(symbols)-1)]
            iterations -= 1
            nSymbols -= 1
        else:
            randomChoice = random.randint(0, 2)
    if randomChoice == 2: #it means number
        if nNumbers > 0:
            password += numbers[random.randint(0, len(numbers)-1)]
            iterations -= 1
            nNumbers -= 1
        else:
            randomChoice = random.randint(0, 2)


print(f"Your new password is : {password}")