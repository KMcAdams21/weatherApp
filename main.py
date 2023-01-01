import requests


# Program to give weather information when given information

# Creating API request
url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&temperature_unit=fahrenheit&timezone=auto&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&current_weather=true"
req = requests.get(url)
wetData = req.json()

# Printing full result for testing means
print(wetData)

# Printing simple weather information
print('The weather for the location at ' + str(wetData['latitude']) + ' ' + str(wetData['longitude']) + ':')
print('The current temperature is ' + str(wetData['current_weather']['temperature']))
print('The current wind speed is ' + str(wetData['current_weather']['windspeed']))
print('The current wind direction is ' + str(wetData['current_weather']['winddirection']))
