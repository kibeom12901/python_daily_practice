import os
import requests
from dotenv import load_dotenv

load_dotenv()

SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_PASSWORD = os.getenv("SHEETY_PASSWORD")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")

class DataManager:
    def __init__(self):
        self.destination_data = []

    def get_sheet_data(self):
        response = requests.get(SHEETY_ENDPOINT, auth=(SHEETY_USERNAME, SHEETY_PASSWORD))
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_sheet_data(self, row_id, new_iata_code):
        put_endpoint = f"{SHEETY_ENDPOINT}/{row_id}"
        new_data = {
            "price": {
                "iataCode": new_iata_code
            }
        }
        response = requests.put(url=put_endpoint, json=new_data, auth=(SHEETY_USERNAME, SHEETY_PASSWORD))
        response.raise_for_status()
        print(f"Row {row_id} updated with iataCode: {new_iata_code}")
