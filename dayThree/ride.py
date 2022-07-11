height = int(input("What is your height ? "))

if height < 120:
    print("Sorry you can't ride.")
else:
    print("You can ride !")
    age = int(input("What is your age ? "))
    if age >= 18:
        print("It will be $12")
    elif age < 12:
        print("It will be $5")
    else:
        print("It will be $7")