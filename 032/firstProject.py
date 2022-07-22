import smtplib 
import random 
import datetime as dt

my_email = "pythontesting67@gmail.com"
password = "zayikltzrvbfjoxj"
#password = "yzdljaithvnoumwu"
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="damastes.versusexcursus@gmail.com ", 
#         msg="Subject:Salut\n\nJe viens de t'envoyer un mail en python.\n Cool hein?"
#         )
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
# dateOfBirth = dt.datetime(year=1995, month=12, day=30)
# print(dateOfBirth)


with open("quotes.txt", mode="r") as file:
    quotes = file.readlines() 
    
now = dt.datetime.now()
day = now.weekday()
if day == 0:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="yanismehalaine@outlook.fr",
            msg=f"Subject:The quote of the week\n\n{random.choice(quotes)}"
        )
    
