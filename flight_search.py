import requests
import os

class FlightSearch:

    def __init__(self):
        self.FLIGHT_URL = "https://tequila-api.kiwi.com/locations/query"
        self.cities = []
        self.iata = []
        self.header = {
            "apikey_loc": os.environ.get("apikey_loc")
        }

    def generate_iata(self):
        for i in range(0, len(self.cities)):
            query = {"term": self.cities[i], "location_types": "city"}
            response = requests.get(url=self.FLIGHT_URL, headers=self.header, params=query)
            data = response.json()["locations"]
            self.iata.append(data[0]["code"])
