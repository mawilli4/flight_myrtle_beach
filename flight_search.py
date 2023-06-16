import requests
from datetime import datetime
from datetime import timedelta
import os


now = datetime.now()
today = now.strftime("%d/%m/%Y")
six_months = (datetime.now() + timedelta(days=362/2)).strftime("%d/%m/%Y")
leave_date = today
return_date = six_months
adults = "2"
children = "1"
min_nights = "3"
max_nights = "5"
max_stops = "2"

# This class is responsible for communicating with Kiwi Tequila Flight Search API


class FlightSearch:
    import os
    from dotenv import load_dotenv
    load_dotenv()

    def __init__(self):
        self.FLIGHT_TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/"
        self.LOCATIONS_QUERY = "locations/query"
        self.PRICE_QUERY = "v2/search"
        self.TEQUILA_API_KEY = os.getenv('TEQUILA_API_KEY_ENV')
        self.tequila_headers = {
            "apikey": self.TEQUILA_API_KEY,
            "Content-Type": "application/json",
        }

    # This method returns IATA city code to Flight Data based on provided City Name #####
    # This demonstration is specific for Chicago to Myrtle Beach flights

    # def get_iata(self, city):
    #     self.tequila_iata_terms = {
    #         "term": city,
    #         "location_types": "city",
    #         "limit": "1"
    #     }
    #
    #     self.iata_response = requests.get(url=f"{self.FLIGHT_TEQUILA_ENDPOINT}{self.LOCATIONS_QUERY}",
    #                                       headers=self.tequila_headers,
    #                                       params=self.tequila_iata_terms
    #                                       )
    #     self.tequila_iata_response = self.iata_response.json()
    #     self.city_code = self.tequila_iata_response["locations"][0]["code"]
    #     return self.city_code

    # This method returns flight data based on provided search criteria #####

    def get_prices(self, departure_city_code, destination_city_code, max_price):

        self.tequila_price_terms = {
            "fly_from": departure_city_code,
            "fly_to": destination_city_code,
            "date_from": leave_date,
            "date_to": return_date,
            "flight_type": "round",
            "nights_in_dst_from": min_nights,
            "nights_in_dst_to": max_nights,
            "price_to": max_price,
            "limit": "1",
            "adults": adults,
            "children": children,
            "curr": "USD",
            "max_stopovers": max_stops,
            # "select_airlines": "NK",
            # "select_airlines_exclude": "TRUE",
        }

        flight_response = requests.get(url=f"{self.FLIGHT_TEQUILA_ENDPOINT}{self.PRICE_QUERY}",
                                       headers=self.tequila_headers,
                                       params=self.tequila_price_terms
                                       )

        self.tequila_flight_response = flight_response.json()
        print(self.tequila_flight_response)
        if self.tequila_flight_response["_results"] == 0:
            self.flight_search_info = False
            print("No Results")
        else:
            self.price = self.tequila_flight_response["data"][0]["price"]
            self.departure_airport = self.tequila_flight_response["data"][0]["flyFrom"]
            self.destination_airport = self.tequila_flight_response["data"][0]["flyTo"]
            self.departure_date = self.tequila_flight_response["data"][0]["route"][0]["local_departure"][:10]
            self.return_date = self.tequila_flight_response["data"][0]["route"][1]["local_departure"][:10]
            self.airline = self.tequila_flight_response["data"][0]["airlines"]
            self.flight_dep = self.tequila_flight_response["data"][0]["route"][0]["flight_no"]
            self.flight_ret = self.tequila_flight_response["data"][0]["route"][1]["flight_no"]
            self.flight_search_info = [self.price,
                                       self.departure_airport,
                                       self.destination_airport,
                                       self.departure_date,
                                       self.return_date,
                                       self.airline,
                                       self.flight_dep,
                                       self.flight_ret,
                                       ]
