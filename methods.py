import geocoder
import requests

# File used to store methods

# Get data from website and make readable
def getLocation():
    ip = geocoder.ip('me')
    lat = ip.lat
    lon = ip.lng
    return lat, lon

# Create api url from latitude and longitude
def sendAPI(lat, lon):
    lat = str(lat)
    lon = str(lon)
    url = "https://api.open-meteo.com/v1/forecast?latitude="+lat+"&longitude="+lon+"&temperature_unit=fahrenheit&timezone=auto&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&current_weather=true"
    req = requests.get(url)
    info = req.json()
    return info