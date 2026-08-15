# # # with open("weather_data.csv") as data_file:
# # #     data = data_file.read()
# # #     print (data)
# # #      too much inconvnient
# #
# # import csv
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperature = []
# #     for row in data:
# #         if row[1]!= "temp":
# #             temperature.append(int(row[1]))
# #
# #     print(temperature)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# ## print(type(data)) #panda data frame object
# #print(data["temp"])  # type is panda series object
# # series is eq to list
#
# data_dict = data.to_dict() #converts data into dictionary
# print(data_dict)
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# # to do : find out avg temp
# # sum_temp = 0
# # for i in range (len(temp_list)):
# #     sum_temp += temp_list[i]
# # average = sum_temp / len(temp_list)
# # print(int(average))
#
# # OR
#
# # average = sum(temp_list) / len(temp_list)
# # print(average)
#
# # OR
# print(int(data["temp"].mean()))
# print(data["temp"].max())
#
# # print(data["condition"]) is same as print(data.condition)
#
# # get data in row
# print(data[data.day == "Monday"])
# # print data when temp was max
# key = data.temp.max()
# print(data[data.temp == key])
#
# #print mondays temp and convert it into fahrenhiet
# monday = data[data.day == "Monday"]
# c_temp = monday.temp
# f_temp = monday.temp* 1.8 + 32
# print(f_temp)
#
# # CREATE A DATAFRAME FROM SCRATCH
# data_dict = {
#     "students": ["amy", "James" ,"Nats"],
#     "score" : [50 , 60 , 90]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260814.csv")
grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
print(red_squirrels)
print(grey_squirrels)
print(black_squirrels)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count" : [grey_squirrels, red_squirrels, black_squirrels]
}
df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")

