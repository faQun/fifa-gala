#!/usr/bin/python3

# This is a small programm testing football-data.org API

import requests
import json


API_token = '8b94b7e21dc44d64982e716d5cad96c2'
headers = {'X-Auth-Token':API_token}

req = requests.get("http://api.football-data.org/v2/teams/18",headers)
response_obj = json.loads(req.text)
print (response_obj)


# connection = http.client.HTTPConnection('api.football-data.org')
# headers = { 'X-Auth-Token': 'YOUR_API_TOKEN' }
# connection.request('GET', '/v2/competitions/DED', None, headers )
# response = json.loads(connection.getresponse().read().decode())
