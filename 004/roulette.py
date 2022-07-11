import random

names = input("Give me everybody's names, seperated by a comma.")

bankers = names.split(",")

print("Who's gonna pay the bill ?")
loser = random.randint(0, len(bankers)-1)
print(f"{bankers[loser]} lost. (s)he must pay the bill")