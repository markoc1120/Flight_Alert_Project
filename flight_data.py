import requests
import datetime as dt
import os

class FlightData:

    def __init__(self):
        self.FLIGHT_URL = "https://tequila-api.kiwi.com/v2/search"
        self.header = {
            "apikey": os.environ.get("apikey_search")
        }
        self.now = dt.datetime.now().strftime("%d/%m/%Y")
        self.expire_date = (dt.datetime.now() + dt.timedelta(weeks=24)).strftime("%d/%m/%Y")
        self.data = []
        self.sheet_data = []
        self.city_from = "BUD"

    def generate_data(self, airport, price):
        query = {"fly_from": self.city_from, "fly_to": airport, "date_from": self.now, "date_to": self.expire_date, "adults": 1,
                 "max_stopovers": 0, "flight_type": "round", "curr": "EUR", "price_to": int(price)}
        response = requests.get(url=self.FLIGHT_URL, headers=self.header, params=query)
        data = response.json()["data"]
        self.data.append([data])
        # print(data)
