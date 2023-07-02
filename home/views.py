from django.shortcuts import render
from django.http import HttpResponse
import requests
import datetime
 
 
def index(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Dhaka'

    appid = 'bca6436871fb41fab53e6fdb5af0b06f'                 #appid = apikey
    URL = 'https://api.openweathermap.org/data/2.5/weather'    #api url
    PARAMS = {'q':city , 'appid': appid, 'units': 'metric'}

    r = requests.get(url=URL, params = PARAMS)
    res= r.json()
    if 'weather' in res and len(res['weather']) > 0:
        description = res['weather'][0]['description']
        icon = res['weather'][0]['icon']
    else:
        description = "N/A"
        icon = "N/A"
    
    if 'main' in res:
        temp = res['main']['temp']
        humidity = res['main']['humidity']
    else:
        temp = "N/A"
        humidity = "N/A"
    day = datetime.date.today()
    return render(request, 'index.html', {'description':description, 'icon':icon, 'temp':temp,'humidity':humidity, 'day':day, 'city':city})