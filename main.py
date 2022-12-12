import json
import datetime as dt 
import requests


lat = "33.44"
lon = "-94.04"
API_KEY = "YOUR_API_KEY"
part = "current"

url = "https://api.openweathermap.org/data/3.0/onecall?lat="+lat+"&lon="+lon+"&exclude="+part+"&appid="+API_KEY

response = requests.get(url).json()
print(response["message"])


