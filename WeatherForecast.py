import requests


def get_weather(city):
    api_address = 'https://api.openweathermap.org/data/2.5/weather?appid=bb6117230fcc0b12b690d5af65178e39&q='
    #city=input('Enter the city name:')
    url=api_address + city
    json_data=requests.get(url).json()
    print(json_data)
    format_add = json_data['main']
    print(format_add)
    print("Weather is {0}. Temperature is minimum {1} degree Celsius and maximum is {2} degree Celsius.".format(json_data['weather'][0]['description'],int(format_add['temp_min'] - 273),int(format_add['temp_max'] - 272)))
    return format_add