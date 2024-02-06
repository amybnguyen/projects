import os
import requests

SHEETY_ENDPOINT = "https://api.sheety.co/6ed32ef7a260aaa751babaac33b53a5c/flightDeals/prices"
SHEETY_USER = os.environ.get("SHEETY_USER", "Sheety User not found")
SHEETY_PASS = os.environ.get("SHEETY_PASS", "Sheety Password not found")

sheety_auth = (SHEETY_USER, SHEETY_PASS)


class DataManager:

    def __init__(self):
        self.destination_data = []

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, auth=sheety_auth)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}",
                                    auth=sheety_auth,
                                    json=new_data)
            print(response.text)
