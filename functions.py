# This file will serve as a function library to be used by core.py
# here is the curl command for the Accuweather api current conditions
# curl -X GET "http://dataservice.accuweather.com/currentconditions/v1/349291?apikey=d1w8pFazvk8uKC7AzmWAxWCNP1mtEZK3&details=true"
import requests
import json

# display current conditions based on key
def get_conditions(key):
    conditions_url = 'https://dataservice.accuweather.com/currentconditions/v1/'f'?apikey={api}'.format(key)
    response = requests.get(conditions_url)
    json_version = response.json()
    print("Current Conditions: {}".format(json_version[0].get('WeatherText')))
    return json_version
    
