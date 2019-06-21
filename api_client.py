import json
import requests

API_KEY = "X35RriQxgbDSeCGrBTNoOPnbwTbV4FYsKyz2YgH8"
BASE_URL = "https://developer.nps.gov/api/v1/"
class ApiClient:
    def parks(state):
        response = requests.get(BASE_URL + "parks", params={'api_key':API_KEY, 'limit':'10', 'stateCode': state})
        return response.json()['data']
