from datetime import datetime
import requests #type: ignore 
import sys


try:
    city = sys.argv[1]
    country = sys.argv[2]
    geoLocRequest = requests.get(f"https://api.opencagedata.com/geocode/v1/json?q={city}, {country}&key=0364e1c2b1ef40afb0e0d9ba644ff011")
    geoLocData = geoLocRequest.json()
    for i in range(len(geoLocData)):
        try:
            print(geoLocData["results"][i]["formatted"])
        except IndexError:
            print("Aucune autre ville n'a été trouvée.")
            break
        
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


    # response = requests.get(url="http://api.open-notify.org/iss-now.json")

    # data = response.json()

    # longitude = data["iss_position"]["longitude"]
    # latitudeData = data["iss_position"]["latitudeData"]

    # iss_position = (longitude, latitudeData)

    # print(iss_position)

    # utcOffset = int(geoLocData["results"][0]["annotations"]["timezone"]["offset_string"][:3])
    # response = requests.get(f"https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}&formatted=0")
    # response.raise_for_status()
    # data = response.json()
    # sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + utcOffset
    # sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + utcOffset

    # print(sunrise)
    # print(sunset)
    

except IndexError:
    print("Vous devez donner une ville et un pays en argument.")
    
