def leap(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    return leap
    
    
year = int(input("Which year do you want to check ? "))

if leap(year):
    print(f"The year {year} is a leap year")
else:
    print(f"the year {year} is not a leap year")