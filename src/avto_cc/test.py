import requests
from django.shortcuts import render

def weather_view(request):
    url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"
    querystring = {"city": "Almaty", "lang": "ru"}
    headers = {
        "X-RapidAPI-Key": "fbdebfb574msh392cfcd133e5ea6p148281jsne746d5653e9d",
        "X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    weather_data = response.json()
    
    return render(request, 'weather.html', {'weather_data': weather_data})