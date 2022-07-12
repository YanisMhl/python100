import art 
import random
from gameData import data 

list = data 
score = 0
print(art.logo)
firstContender = random.choice(data)
secondContender = random.choice(data)
print(firstContender["name"])
print(f"Against B: {data[0]}, a, from")

