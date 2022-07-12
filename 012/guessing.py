import random
import art 

replay = True 


#display
print("Welcome to the Number Guessing Game!")

while replay:
    
    #declare variables
    lives = 0
    number = 0
    win = False 
    
    print(art.logo)
    print("I'm thinking of a number between 1 and 100")
    difficulty = input("Type 'easy' or 'hard': ")

    if difficulty == 'hard':
        lives = 5
    else:
        lives = 10
        
    number = random.randint(1, 100)

    while lives > 0 and not win:
        print(f"You have {lives} attempts remaining to guess the number")
        guess = int(input("Make a guess : "))
        if guess > number:
            lives -= 1
            print("Too high.\nGuess again.")
        elif guess < number:
            print("Too low.\nGuess again.")
            lives -= 1
        else:
            win = True 
        
    if win:
        playAgain = input(f"You have won ! The number was {number} ! Do you want to play again ? Type 'y' or 'n' : ")
    else:
        playAgain = input(f"You have lost. The number was {number}. Do you want to play again ? Type 'y' or 'n' : ")
    if playAgain == 'n':
        replay = False
    