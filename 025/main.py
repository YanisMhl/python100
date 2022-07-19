import csv 

# data = []
# with open("weather_data.csv") as file:
#     data = file.readlines()
# print(data)

with open("weather_data.csv") as dataFile:
    data = csv.reader(dataFile)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(row[1])

print(temperatures)