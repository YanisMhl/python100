import requests #type: ignore 

response = requests.get(url="http://api.open-notify.org/iss-now.json")

data = response.json()
print(data)