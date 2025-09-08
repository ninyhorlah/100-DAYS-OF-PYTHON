# import csv 

# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for col in data:
#         if col[1] != "temp":
#             temperature.append(int(col[1]))

#     print(temperature)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# print(data["temp"].min())
# print(data["temp"].max())

# print(data[data.temp == data["temp"].max()])

# temp = (data[data.day == "Monday"])
# print(temp.temp * 9/5 + 32)

data = pandas.read_csv("Squirrel_CensusData.csv")

gray_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])

print(gray_squirrel, red_squirrel, black_squirrel)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel, red_squirrel, black_squirrel]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")