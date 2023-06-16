from flight_search import FlightSearch
from notification_manager import NotificationManager

# This class manages communication between other classes and processes data


class FlightData:

    def __init__(self, departure_city, departure_city_code, destination_city_code, max_price):
        self.departure_city = departure_city
        self.departure_city_code = departure_city_code
        self.destination_city_code = destination_city_code
        self.max_price = max_price

    def search(self):
        flight_search_object = FlightSearch()
        notification_manager_object = NotificationManager()

        flight_search_object.get_prices(self.departure_city_code, self.destination_city_code, self.max_price)

        # Send message with flights meeting criteria
        if flight_search_object.flight_search_info:
            notification_manager_object.send_message(self.departure_city_code, self.destination_city_code,
                                                     flight_search_object.flight_search_info)


