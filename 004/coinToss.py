import random

toss = random.randint(0, 1)

if toss == 0:
    print(f"{toss} : head")
else:
    print(f"{toss} : tails")