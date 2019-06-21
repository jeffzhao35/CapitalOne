import json
import requests

API_KEY = "X35RriQxgbDSeCGrBTNoOPnbwTbV4FYsKyz2YgH8"
BASE_URL = "https://developer.nps.gov/api/v1/"

class ApiClient:
    def parks(state):
        params = {'api_key': API_KEY, 'limit': 10}
        if state:
            params['stateCode'] = state
        response = requests.get(BASE_URL + "parks", params=params)
        return response.json()['data']
