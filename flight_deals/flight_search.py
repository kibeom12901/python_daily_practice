import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv() 

IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations" 
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

class FlightSearch:
    def __init__(self):
        self._api_key = os.environ["AMADEUS_API_KEY"]
        self._api_secret = os.environ["AMADEUS_API_SECRET"]
        self._token = self._get_new_token()

    def _get_new_token(self):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=headers, data=body)
        response.raise_for_status()
        token = response.json()['access_token']
        print(f"Your token is {token}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return token

    def get_iata_code(self, city_name):
        headers = {"Authorization": f"Bearer {self._token}"}
        query_params = {
            "keyword": city_name,
            "subType": "CITY",
        }
        response = requests.get(IATA_ENDPOINT, headers=headers, params=query_params)
        print(f"Status code {response.status_code}. Response: {response.text}")
        data = response.json().get('data', [])
        for location in data:
            if location.get('iataCode'):
                return location['iataCode']
        return "Not Found"

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "10",
        }
        response = requests.get(url=FLIGHT_ENDPOINT, headers=headers, params=query)
        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search. Check the API documentation for details.")
            print("Response body:", response.text)
            return None
        return response.json()
