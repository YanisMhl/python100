import csv 
import pandas 

# # data = []
# # with open("weather_data.csv") as file:
# #     data = file.readlines()
# # print(data)

# # with open("weather_data.csv") as dataFile:
# #     data = csv.reader(dataFile)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(row[1])

# # print(temperatures)

# data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# # print(data_dict)

# # tempList = data["temp"].to_list()
# # print(tempList)
# # print(data["temp"].mean())
# # maxTemp = data["temp"].max()
# # print(f"The maximum temperature is : {maxTemp}")

# print(data[data["day"] == "Monday"])
# print(data[data["temp"] == data["temp"].max()])

# #Create a dataframe from scratch
# dataDict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(dataDict)
# data.to_csv("newData.csv")

data = pandas.read_csv("2018CentralParkSquirrelsData.csv")
squirrelCount = {
    "Fur Color": [],
    "Count": []
}
#print(data["Primary Fur Color"])
FurList = data["Primary Fur Color"].to_list()

for fur in FurList:
    if fur not in squirrelCount["Fur Color"]:
        squirrelCount["Fur Color"].append(fur)
        squirrelCount["Count"].append(0)
    else:
        for i in range(len(squirrelCount["Fur Color"])):
            if fur == squirrelCount["Fur Color"][i]:
                squirrelCount["Count"][i] += 1
                

sheet = pandas.DataFrame(squirrelCount)
sheet.to_csv("squirrel_count.csv")
        
