import requests
import methods
import tkinter as tk

# Program to give weather information when given information

# Get location of device
lat, lon, address = methods.getLocation()
city = address.get('city','')

# Getting weather information using API
wetData = methods.sendAPI(lat, lon)

# Printing simple weather information
lat = 'The weather for '+ city + ':'
lon = 'The current temperature is ' + str(wetData['current_weather']['temperature']) + ' deg F'
windSpeed = 'The current wind speed is ' + str(wetData['current_weather']['windspeed']) + ' mph'
windDir = 'The current wind direction is ' + str(wetData['current_weather']['winddirection'])

# Creating a tkinter window to display information
window = tk.Tk()
window.title("Current Weather")
window.geometry("800x300")

latDis = tk.Label(text=lat, font=("Arial", 24, "bold"))
latDis.pack(padx=5, pady=10)

lonDis = tk.Label(text=lon, font=("Arial", 24, "bold"))
lonDis.pack(padx=5, pady=10)

winSpeedDis = tk.Label(text=windSpeed, font=("Arial", 24, "bold"))
winSpeedDis.pack(padx=5, pady=10)

winDirDis = tk.Label(text=windDir, font=("Arial", 24, "bold"))
winDirDis.pack(padx=5, pady=10)

window.mainloop()