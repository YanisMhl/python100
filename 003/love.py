print("Welcome to the Love Calculator!")
name1 = input("What is your name ? ")
name2 = input("What is their name ? ")

true = 0
love = 0

t = name1.lower().count("t") + name2.lower().count("t")
true += t
r = name1.lower().count("r") + name2.lower().count("r")
true += r
u = name1.lower().count("u") + name2.lower().count("u")
true += u
e = name1.lower().count("e") + name2.lower().count("e")
true += e

print(f"T occurs {t} times\nR occurs{r} times\nU occurrs {u} times\nE occurs {e} times")
print("Total = " + str(true) + "\n")

l = name1.lower().count("l") + name2.lower().count("l")
love += l
o = name1.lower().count("o") + name2.lower().count("o")
love += o
v = name1.lower().count("v") + name2.lower().count("v")
love += v 
love += e

print(f"L occurs {l} times\nO occurs{o} times\nV occurrs {v} times\nE occurs {e} times")
print("Total = " + str(love) + "\n")

loveScore = int(str(true) + str(love))

if loveScore < 10 or loveScore > 90:
    print(f"Your score is {loveScore}, you go together like coke and mentos")
elif loveScore >= 40 and loveScore <= 50:
    print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f"Your score is {loveScore}")
