from dotenv import load_dotenv
from flight_data import FlightData
#  Tequila Search API Documentation "https://tequila.kiwi.com/docs/tequila_api/search_api"

load_dotenv()

DEPARTURE_CITY = "Chicago"
DEPARTURE_CITY_CODE = "CHI"
DESTINATION_CITY_CODE = "MYR"
MAX_PRICE = "5000"

flight_data_object = FlightData(DEPARTURE_CITY, DEPARTURE_CITY_CODE, DESTINATION_CITY_CODE, MAX_PRICE)
flight_data_object.search()


