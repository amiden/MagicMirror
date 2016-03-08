#simple GUI

from Tkinter import *

#create the window
root = Tk()

#modify root window
root.title("Weather")
root.geometry("200x100")

import pyowm

owm = pyowm.OWM('3526f14542bc7277002d2cbb0dee8424')

# You have a pro subscription? Use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# Will it be sunny tomorrow at this time in Milan (Italy) ?
forecast = owm.daily_forecast("Milan,it")
tomorrow = pyowm.timeutils.tomorrow()
forecast.will_be_sunny_at(tomorrow)  # Always True in Italy, right? ;-)

# Search for current weather in London (UK)
observation = owm.weather_at_place('London,uk')
w = observation.get_weather()
print(w.get_wind())                      # <Weather - reference time=2013-12-18 09:20,
# status=Clouds>

# Weather details
w.get_wind()                  # {'speed': 4.6, 'deg': 330}
w.get_humidity()              # 87
w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
observation_list = owm.weather_around_coords(-22.57, -43.12)

#!/usr/bin/env python
from urllib2 import urlopen
from contextlib import closing
import json


# Automatically geolocate the connecting IP
url = 'http://freegeoip.net/json/'
try:
    with closing(urlopen(url)) as response:
        location = json.loads(response.read())
        print(location['zip_code'])
        #print(location)
        location_zip = location['zip_code']
except:
    print("Location could not be determined automatically")

# Search for weather at Zipcode
url1 = 'http://api.openweathermap.org/data/2.5/weather?zip='
url2 = location_zip
url3 = ',us&appid=3526f14542bc7277002d2cbb0dee8424'
urlTemp = url1 + url2 + url3
try:
    with closing(urlopen(urlTemp)) as response:
        data = json.loads(response.read())
            temp = data['main']['temp']
                temperature = temp*9/5-459.67
                print(temperature)
                print(data['weather'][0]['id'])
except:
    print("no kittez")

#kick off the event loop
root.mainloop()