import smtplib
import random
import pandas
import datetime as dt

my_email = "pythontesting67@gmail.com"
password = "zayikltzrvbfjoxj"

##################### Extra Hard Starting Project ######################

def checkBirthday(birthdayList):
    now = dt.datetime.now()
    for i in range(len(birthdayList)):
        if now.month == birthdayList[i].month and now.day == birthdayList[i].day:
            return i
    return -1

def pickRandomLetter():
    i = random.randint(1, 3)
    letter = "letter_templates/letter_" + str(i) + ".txt"
    with open(letter, mode="r") as file:
        result = file.read()
    return result


# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv").to_dict()
names = []
emails = []
years = []
months = []
days = []
birthdays = []

for key in data["name"]:
    names.append(data["name"][key])
for key in data["email"]:
    emails.append(data["email"][key])
for key in data["year"]:
    years.append(data["year"][key])
for key in data["month"]:
    months.append(data["month"][key])
for key in data["day"]:
    days.append(data["day"][key])
    
for i in range(len(years)):
    birthdays.append(dt.datetime(year=years[i], month=months[i], day=days[i]))    
    
if checkBirthday(birthdays) != -1:
    letter = pickRandomLetter().replace("[NAME]", names[checkBirthday(birthdays)])
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=emails[checkBirthday(birthdays)],
            msg=f"Subject:Happy Birthday!!\n\n{letter}"
            )


