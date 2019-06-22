import json
import requests

API_KEY = "X35RriQxgbDSeCGrBTNoOPnbwTbV4FYsKyz2YgH8"
BASE_URL = "https://developer.nps.gov/api/v1/"
class ApiClient:
    def parks(park_name, state, designation, keyword):
        response = requests.get(BASE_URL + "parks", params={'api_key':API_KEY, 'limit':'50', 'parkCode': park_name, 'stateCode': state, 'q': designation, 'q': keyword})
        return response.json()['data']
