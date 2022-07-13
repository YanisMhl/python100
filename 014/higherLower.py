import art 
import random
from gameData import data 

def format_data(contender):
    contenderName = contender["name"]
    contenderDescription = contender["description"]
    contenderCountry = contender["country"]
    return f"{contenderName}, a {contenderDescription}, from {contenderCountry}"

def contenderName(contender):
    return contender["name"]

def contenderFollowers(contender):
    return contender["follower_count"]

def announceWin(winner, loser):
    print(f"Congratulations ! You win ! {contenderName(winner)} has more followers than {contenderName(loser)} ({contenderFollowers(winner)}M VS. {contenderFollowers(loser)}M)")

def announceLose(loser, winner):
    print(f"Sorry You lose. {contenderName(loser)} has not more followers than {contenderName(winner)} ({contenderFollowers(loser)}M VS. {contenderFollowers(winner)}M)")



#Display logo
print(art.logo)

#Initialize variables
score = 0
firstContender = random.choice(data)
secondContender = random.choice(data)

#Display the contenders
print(f"Compare A: {format_data(firstContender)}")
print(f"Against B: {format_data(secondContender)}")

#Ask input from user
answer = input("Who has more followers? Type 'A' or 'B': ")

if answer == 'A':
    if contenderFollowers(firstContender) > contenderFollowers(secondContender):
        #he wins
        announceWin(firstContender, secondContender)
    else:
        #he loses
        announceLose(firstContender, secondContender)
        
elif answer == 'B':
    if contenderFollowers(secondContender) >= contenderFollowers(firstContender):
        #he wins
        announceWin(secondContender, firstContender)
    else:
        #he loses
        announceLose(secondContender, firstContender)

    


