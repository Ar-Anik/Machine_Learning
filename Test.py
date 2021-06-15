import pandas

weather = {
    'Day' : ['15/6/2021', '16/6/2021', '17/6/2021', '18/6/2021', '19/6/2021', '20/6/2021'],
    'Temperature' : [32, 35, 28, 24, 32, 32],
    'windspeed' : [6, 7, 2, 7, 4, 2],
    'event' : ['Rain', 'Sunny', 'Snow', 'Snow', 'Rain', 'Sunny']
}

data = pandas.DataFrame(weather)
print(data)

print(data.head(2))
print(data.tail(3))
