# This is the core file which will run our project
# here is the curl command for the Accuweather api current conditions
# curl -X GET "http://dataservice.accuweather.com/currentconditions/v1/349291?apikey=d1w8pFazvk8uKC7AzmWAxWCNP1mtEZK3&details=true"
import requests
import json
import functions

# get the current conditions for Omaha: 349291 is the location key for Omaha
response = functions.get_conditions(349291)

functions.print_HistoryData()
