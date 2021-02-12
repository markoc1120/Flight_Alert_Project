from twilio.rest import Client
import os


class NotificationManager:

    def __init__(self, airports, prices, city_from, times, cities):
        self.airports = airports
        self.times = times
        self.prices = prices
        self.cities = cities
        self.city_from = city_from
        self.ACC_SID = os.environ.get("ACC_SID")
        self.AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
        self.PHONE_FROM = "+12513331821"
        self.PHONE_TO = os.environ.get("PHONE_TO")
        self.client = Client(self.ACC_SID, self.AUTH_TOKEN)

    def making_notification(self):

        for i in range(0, len(self.airports)):
            if len(self.prices[i]) != 0:
                low_price = min(self.prices[i])
                index = self.prices[i].index(low_price)
                message = self.client.messages \
                    .create(
                    body=f"Low price alert! Only {low_price} EUR to fly from Budapest-{self.city_from} to "
                         f"{self.cities[i]}-{self.airports[i]} with a departure time of {''.join(self.times[i][index])}",
                    from_=self.PHONE_FROM,
                    to=self.PHONE_TO
                )
                print(message.status)
