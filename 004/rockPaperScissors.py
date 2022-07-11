import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computerChoice = random.randint(0, 2)

if choice == 0:
    print("You chose Rock")
    if computerChoice == 0:
        print("Computer chose Rock.\nIt's a tie.")
    elif computerChoice == 1:
        print("Computer chose Paper.\nYou lose.")
    else:
        print("Computer chose scissors.\nYou win.")
elif choice == 1:
    print("You chose Paper")
    if computerChoice == 0:
        print("Computer chose Rock.\nYou win.")
    elif computerChoice == 1:
        print("Computer chose Paper.\nIt's a tie.")
    else:
        print("Computer chose scissors.\nYou lose.")
else:
    print("You chose Scissors")
    if computerChoice == 0:
        print("Computer chose Rock.\nYou lose.")
    elif computerChoice == 1:
        print("Computer chose Paper.\nYou win.")
    else:
        print("Computer chose scissors.\nIt's a tie.")