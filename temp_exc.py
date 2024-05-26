# # with list

# arr = []

# with open("nyc_weather.csv","r") as f:
#     for line in f:
#         tokens = line.split(',')
#         try:
#             temperature = int(tokens[1])
#             arr.append(temperature)
#         except:
#             print("Invalid temperature.Ignore the row")


# # What was the average temperature in first week of Jan
# avg = sum( arr[:8] )/7
# print(avg)
# # What was the maximum temperature in first 10 days of Jan
# print( max(arr[:11]))

# with dict

dict = {}
with open("nyc_weather.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        try:
            temperature = int(tokens[1])
            dict[ tokens[0] ] = int(tokens[1])
        except:
            print("Invalid temperature.Ignore the row")

# What was the temperature on Jan 9?
print(dict['Jan 9'])
# What was the temperature on Jan 4?
print(dict['Jan 4'])