import random

def hasUnderscore(word):
    result = False
    for c in word:
        if c == ' ':
            result = True 
    return result             

#Déclaration
display = []
wordList = ["ardvark", "baboon", "camel"]
lives = 3 

#Initialisation directe
chosenWord = wordList[random.randint(0, len(wordList)-1)]

for c in chosenWord:
    display.append(" ")
    

#boucle de jeu
while hasUnderscore(display) and lives > 0:
    found = False 
    print(display)
    guess = input("guess a letter from the word : ").lower()

    for i in range(0, len(chosenWord)):
        if guess == chosenWord[i]:
            display[i] = chosenWord[i]
            found = True 
    
    if not found:
        lives -= 1
        print(f"Wrong. This letter is not in the word. You just lost a life :(\nYou still have {lives} lives.")
    else:
        print("You're correct !")
        

if lives < 1:
    print(f"You lost, sorry :(\nThe word was {chosenWord}")
else:
    print(f"You win !!!! Yes the word was {chosenWord}")