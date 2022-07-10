age = int(input("What is your current age ? "))

yearsLeft = 90 - age
weeks = 52 * yearsLeft
days = 365 * yearsLeft
months = 12 * yearsLeft

print(f"You have {days} days, {weeks} weeks, and {months} months left. (if you live until you're 90)")