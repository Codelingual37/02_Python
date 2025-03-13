import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250306.csv")
gray = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cinnamon = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

color_dict = {
	"Fur Color": ["Gray", "Black", "Cinnamon"],
	"Count": [gray, black, cinnamon]
}

data = pandas.DataFrame(color_dict)
data.to_csv("fur_color.csv")

