import geocoder
import requests
from geopy.geocoders import Nominatim

# File used to store methods

# Get data from website and make readable
def getLocation():
    # Get IP address location
    ip = geocoder.ip('me')
    lat = ip.lat
    lon = ip.lng
    # Get address from lat and long
    geolocator = Nominatim(user_agent='weatherApp')
    locate = geolocator.reverse(str(lat)+','+str(lon))
    address = locate.raw['address']
    return lat, lon, address

# Create api url from latitude and longitude
def sendAPI(lat, lon):
    # Merge lat and long into url to get weather info
    lat = str(lat)
    lon = str(lon)
    url = "https://api.open-meteo.com/v1/forecast?latitude="+lat+"&longitude="+lon+"&temperature_unit=fahrenheit&precipitation_unit=inch&timezone=auto&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&current_weather=true"
    # Send API request and get weather info
    req = requests.get(url)
    info = req.json()
    return info