

travel_log = [
    {
        "country": "France",
        "visits": 3,
        "cities": ["Paris", "Marseille", "Toulouse"]
    },
    
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]

def add_new_country(country, visits, cities):
    newCountry = {}
    newCountry["country"] = country
    newCountry["visits"] = visits
    newCountry["cities"] = cities
    travel_log.append(newCountry)
    

add_new_country("Russia", 7, ["Moscow", "St-Petersburg"])

print(travel_log)

