print("Welcome to the tip calculator.")
totalBill = float(input("What was the total bill ? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15 ? "))
people = int(input("How many people to split the bill ? "))

rate = (totalBill/100)*tip
finalBill = round((totalBill+tip)/people, 2)

print(f"Each person should pay: {finalBill}")