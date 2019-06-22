import json
import requests

API_KEY = "X35RriQxgbDSeCGrBTNoOPnbwTbV4FYsKyz2YgH8"
BASE_URL = "https://developer.nps.gov/api/v1/"

class ApiClient:
    def parks(park_name, state, designation, keyword):
        params={'api_key':API_KEY, 'limit':'50', 'parkCode': park_name, 'stateCode': state, 'q': designation, 'q2': keyword}
        if state:
        	params['parkCode'] = park_name
            params['stateCode'] = state
            params['q'] = designation
            params['q2'] = keyword
        response = requests.get(BASE_URL + "parks", params=params)
        return response.json()['data']
