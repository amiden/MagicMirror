#simple GUI

from Tkinter import *
from PIL import Image, ImageTk
import time
import pyowm
#!/usr/bin/env python
from urllib2 import urlopen
from contextlib import closing
import json

#create the window
root = Tk()

#modify root window
root.title("Weather")
root.geometry("480x800")
#root.overrideredirect(1)
root.configure(background='black')
w = Canvas(root, width=480, height=800, bg="black")
# (x0, y0, x1, y1)
w.create_line(0, 400, 480, 400, fill="white")
w.pack()

owm = pyowm.OWM('3526f14542bc7277002d2cbb0dee8424')

# You have a pro subscription? Use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# Will it be sunny tomorrow at this time in Milan (Italy) ?
forecast = owm.daily_forecast("Milan,it")
tomorrow = pyowm.timeutils.tomorrow()
forecast.will_be_sunny_at(tomorrow)  # Always True in Italy, right? ;-)

# Search for current weather in London (UK)
observation = owm.weather_at_place('London,uk')
wea = observation.get_weather()
#print(w.get_wind())                      # <Weather - reference time=2013-12-18 09:20,
# status=Clouds>

# Weather details
wea.get_wind()                  # {'speed': 4.6, 'deg': 330}
wea.get_humidity()              # 87
wea.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
observation_list = owm.weather_around_coords(-22.57, -43.12)

# Automatically geolocate the connecting IP
url = 'http://freegeoip.net/json/'
#while True:
try:
    with closing(urlopen(url)) as response:
        location = json.loads(response.read())
            #print(location['zip_code'])
            #print(lcoation['city'])
            print(location)
                location_zip = location['zip_code']
#break
except:
    #time.sleep(1)
    #continue
    print("didn't find ip")

# Search for weather at Zipcode
url1 = 'http://api.openweathermap.org/data/2.5/weather?zip='
url2 = '55423'
url3 = ',us&appid=3526f14542bc7277002d2cbb0dee8424'
urlTemp = url1 + url2 + url3
try:
    with closing(urlopen(urlTemp)) as response:
        data = json.loads(response.read())
            #print(data)
            temp = data['main']['temp']
                temperature = temp*9/5-459.67
                #print(temperature)
                #print(data['weather'][0]['id'])
                weatherId = data['weather'][0]['id']
except:
    print("no kittez")

#
# check what the id is and put appropriate picture
# http://openweathermap.org/weather-conditions
if weatherId == 800:
    
    load = Image.open("clear.png")
        render = ImageTk.PhotoImage(load)
        
        # labels can be text or images
        img = Label(root, borderwidth=0, highlightthickness=0, image=render)
        img.image = render
        img.place(x=176, y=260)
        
        with Image.open("clear.png") as image:
            width, height = image.size
#print("w: " + str(width))
#print("h: " + str(height))

else:
    print(weatherId)
temperature = int(temperature)
temperature = str(temperature)
degree_sign = u'\N{DEGREE SIGN}'
temperature = temperature + degree_sign
#text = w.create_text(0, 120, justify = CENTER, fill="white",font="Times 20 bold", text = )
#
w.create_text(240, 80, fill = "white", font = "Veranda 70 bold", text = "Minneapolis")
w.create_text(240,180,fill="white",font="Veranda 120 bold",
              text = temperature)
#
#w.pack()
#kick off the event loop
root.mainloop()