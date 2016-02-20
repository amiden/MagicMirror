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
        location_zip = location['zip_code']
except:
    print("Location could not be determined automatically")

#kick off the event loop
root.mainloop()