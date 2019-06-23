import json
import requests

API_KEY = "X35RriQxgbDSeCGrBTNoOPnbwTbV4FYsKyz2YgH8"
BASE_URL = "https://developer.nps.gov/api/v1/"

class ApiClient:
	def parks(park_name, state, designation, keyword):
		params={'api_key':API_KEY, 'limit':'50'}
		if park_name:
			params['parkCode'] = park_name
		if state:
			params['stateCode'] = state
		if designation:
			params['q'] = designation
		if keyword:
			params['q'] = keyword
		response = requests.get(BASE_URL + "parks", params=params)
		return response.json()['data']
