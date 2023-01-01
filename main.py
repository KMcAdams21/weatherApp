import requests
import methods

# Program to give weather information when given information

# Get location of device
lat, lon = methods.getLocation()

# Getting weather information using API
wetData = methods.sendAPI(lat, lon)

# Printing full result for testing means
print(wetData)

# Printing simple weather information
print('The weather for the location at ' + str(wetData['latitude']) + ' ' + str(wetData['longitude']) + ':')
print('The current temperature is ' + str(wetData['current_weather']['temperature']))
print('The current wind speed is ' + str(wetData['current_weather']['windspeed']))
print('The current wind direction is ' + str(wetData['current_weather']['winddirection']))
