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

def days_in_month(year, month):
    months_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap(year) and month == 2:
        return 29
    else:
        return months_day[month-1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(f"There are {days} days")