import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

class PasswordGenerator:
    
    def __init__(self, letters, symbols, numbers):
        self.password=""
        self.randomChoice = 0
        self.nLetters = letters
        self.nSymbols = symbols 
        self.nNumbers = numbers 
        self.iterations = self.nNumbers + self.nSymbols + self.nNumbers

    def generate(self):
        while self.iterations > 0:
            randomChoice = random.randint(0, 2)
            if randomChoice == 0: #it means letter
                if self.nLetters > 0:
                    self.password += letters[random.randint(0, len(letters)-1)]
                    self.iterations -= 1
                    self.nLetters -= 1
                else:
                    randomChoice = random.randint(0, 2)
            if randomChoice == 1: #it means symbol
                if self.nSymbols > 0:
                    self.password += symbols[random.randint(0, len(symbols)-1)]
                    self.iterations -= 1
                    self.nSymbols -= 1
                else:
                    randomChoice = random.randint(0, 2)
            if randomChoice == 2: #it means number
                if self.nNumbers > 0:
                    self.password += numbers[random.randint(0, len(numbers)-1)]
                    self.iterations -= 1
                    self.nNumbers -= 1
                else:
                    randomChoice = random.randint(0, 2)


