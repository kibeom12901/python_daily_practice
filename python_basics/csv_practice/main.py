
import pandas
import math

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250204.csv")

gray_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])

print(gray_squirrel, cinnamon_squirrel, black_squirrel)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel, cinnamon_squirrel, black_squirrel]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")



# temp_list = data["temp"].to_list()

# print(data["temp"].mean())
# print(data["temp"].max())

# print(data["condition"])
# print(data.condition)

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp
