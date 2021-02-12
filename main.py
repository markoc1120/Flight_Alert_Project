from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager


datamanager = DataManager()
flightdata = FlightData()
flightsearch = FlightSearch()


datamanager.getting_sheet_data()

sheet_data = datamanager.data
# print(sheet_data)

if len(sheet_data[0]["iata"]) == 0:
    flightsearch.cities = [sheet_data[i]["city"] for i in range(0, len(sheet_data))]
    flightsearch.generate_iata()
    datamanager.writing_iata(flightsearch.iata)

airports = []
cities = []
for i in range(0, len(sheet_data)):
    airport = sheet_data[i]["iata"]
    airports.append(airport)
    price = sheet_data[i]["lowestPrice"]
    cities.append(sheet_data[i]["city"])
    flightdata.sheet_data.append([airport, price])
    flightdata.generate_data(airport, price)

prices = []
times = []
for item in flightdata.data:
    for subitem in item:
        subprices = []
        subtimes = []
        for i in range(0, len(subitem)):
            subprices.append(subitem[i]["price"])
            subtimes.append(subitem[i]["utc_departure"][:10])
        prices.append(subprices)
        times.append(subtimes)

print(times)
notification_manager = NotificationManager(airports, prices, flightdata.city_from, times, cities)
notification_manager.making_notification()
