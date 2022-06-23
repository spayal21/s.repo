#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import os
from datetime import datetime

user_api=os.environ['Current weather data']
location=input("ENTER THE CITY NAME  : ")
#https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
complete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
api_link=requests.get(complete_api_link)
api_data=api_link.json()
#print(api_data)
#creating variables to store data from api and display
if api_data['cod']=='404':
    print("Invalid city: {},Please check your city name",format(location))
else: 
    temp_city=((api_data['main']['temp'])-273.15)
    weather_desc=(api_data['weather'][0]['description'])
    hmdt=api_data['main']['humidity']
    wind_spd=api_data['wind']['speed']
    date_time=datetime.now().strftime("%d %b %Y | %I:%M:%S%p")

print("----------------------------------------------------------------")   
print("Weather stats for - {} || {}".format(location.upper(),date_time))
print("----------------------------------------------------------------")   



print("CURRENT TEMPERATURE IS : {:.2f} deg C".format(temp_city))
print("CURRENT WEATHER DESCRIPTION :",weather_desc)
print("CURRENT HUMIDITY :",hmdt,'%')
print("CURRENT WIND SPEED :",wind_spd,'kmph')


                                  

                     
    

                                            





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




