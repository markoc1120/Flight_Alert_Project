import requests
import os


class DataManager:

    def __init__(self):
        self.ID = 2
        self.SHEET_URL_GET = os.environ.get("SHEET_GET")
        self.SHEET_URL_POST = os.environ.get("SHEET_POST")
        self.USERNAME = os.environ.get("USERNAME")
        self.PASSWORD = os.environ.get("PASSWORD")
        self.data = None

    def getting_sheet_data(self):
        response = requests.get(url=self.SHEET_URL_GET, auth=(self.USERNAME, self.PASSWORD))
        response.raise_for_status()
        data = response.json()
        self.data = data["sheet1"]
        # print(data)

    def writing_iata(self, iatas):
        for i in range(0, len(iatas)):
            SHEET_URL_PUT = f"{os.environ.get('SHEET_PUT')}{i+2}"
            params = {
                "sheet1": {
                    "iata": iatas[i]
                }
            }
            requests.put(url=SHEET_URL_PUT, auth=(self.USERNAME, self.PASSWORD), json=params)

