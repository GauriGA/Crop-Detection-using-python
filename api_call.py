import pandas as pd
import requests
import json
def api_call():
    apis="4f0a5dad25ab2d47db91ec21ebd4053d"
    cities="delhi"
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+cities+"&appid="+apis)
    #print(response.text)
    dictionary=json.loads(response.text)
    dict2=(dictionary['main'])
    avg_temp=((dict2['temp_min']+dict2['temp_max'])/2)
    humidity=dict2['humidity']
    return avg_temp,humidity


