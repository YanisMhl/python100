import smtplib
from datetime import datetime
import requests #type: ignore 
import sys

my_email = "pythontesting67@gmail.com"
password = "zayikltzrvbfjoxj"
weatherKey = "e90c96659f7f42e485daafb80a89e351"
city = "strasbourg"
country = "fr"
geoLocRequest = requests.get(f"https://api.opencagedata.com/geocode/v1/json?q={city}, {country}&key=0364e1c2b1ef40afb0e0d9ba644ff011")
geoLocRequest.raise_for_status()
geoLocData = geoLocRequest.json()
        
parameters = {
    "lat": geoLocData["results"][0]["annotations"]["DMS"]["lat"],
    "lng": geoLocData["results"][0]["annotations"]["DMS"]["lng"]
    }
    
    
#Formatting latitude and longitude
latitude = parameters["lat"].replace('\'', '').replace('°','').replace(' ', '-')
latitude = latitude[:-2] + latitude[-1:]
longitude = parameters["lng"].replace('\'', '').replace('°','').replace(' ', '-')
longitude = longitude[:-2] + longitude[-1:]

latitude = sum(float(x) / 60 ** n for n, x in enumerate(latitude[:-1].split('-')))  * (1 if 'N' in latitude[-1] else -1)
longitude = sum(float(x) / 60 ** n for n, x in enumerate(longitude[:-1].split('-'))) * (1 if 'E' in longitude[-1] else -1)
    
print(f"{latitude}\n{longitude}") 

weatherParameters={
    "lat": latitude,
    "lon": longitude,
    "appid": weatherKey,
    "exclude": "current,minutely,daily"
}

weatherRequest = requests.get(f"https://api.openweathermap.org/data/2.5/onecall", params=weatherParameters)
weatherRequest.raise_for_status()
weatherData = weatherRequest.json()
weatherSlice = weatherData["hourly"][:12]
finalMessage = "Don't bring an umbrella."
for hourData in weatherSlice:
    conditionCode = hourData["weather"][0]["id"]
    if int(conditionCode) < 700:
        finalMessage = "Bring an umbrella"
        

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
            from_addr=my_email,
            to_addrs="yanismehalaine@outlook.fr",
            msg=f"Subject:Meteo prediction\n\n{finalMessage}"
            )

    