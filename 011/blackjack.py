MAX_SCORE = 21
import random
from typing import final 

def calculateScore(cards):
    score = 0
    for card in cards:
        score += card
    return score 

cards = []
computerCards = []
score = 0
computerScore = 0
finalCards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
replay = True

print('''88          88                       88        88                       88         
88          88                       88        ""                       88         
88          88                       88                                 88         
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                              ,88                                  
                                            888P"   ''')

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")



while replay:
    if play == 'y':
        cards.append(random.choice(finalCards))
        cards.append(random.choice(finalCards))
        score = calculateScore(cards)
        computerCards.append(random.choice(finalCards))
        computerCards.append(random.choice(finalCards))
        computerScore = calculateScore(computerCards)
        print(f"Your cards: {cards}, current score: {score}")
        anotherCard = input("Type 'y' to get another card, type 'n' to pass: ")
        if anotherCard == 'y':
            cards.append(random.choice(finalCards))
            score = calculateScore(cards)
            #computerCards.append(random.randint(1, 10))
            #computerScore = calculateScore(computerCards)
        print(f"Your final hand: {cards}, final score: {score}")
        print(f"Computer's final hand: {computerCards}, final score: {computerScore}")
        if score > MAX_SCORE:
            print("You went over. You lose.")
        elif computerScore > score:
            print("Computer beats you. You lose.")
        elif computerScore == score:
            print("It's a draw")
        else:
            print("You won !")
        
        playAgain = input("Do you want to play another game ? type 'y' for yes or 'n' for no: ")
        if playAgain == 'n':
            replay = False
            
        cards.clear()
        computerCards.clear()

        