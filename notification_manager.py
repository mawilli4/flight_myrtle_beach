# from twilio.rest import Client
# Note: The text notification section no longer works as Twilio no longer offers a free tier.
import smtplib
import os

class NotificationManager:

    def __init__(self):
        # self.twilio_account_sid = "personal information removed"
        # self.twilio_auth_token = "personal information removed"
        self.MY_SEND_EMAIL = os.getenv('MY_SEND_EMAIL')
        self.SEND_EMAIL_PASSWORD = os.getenv('SEND_EMAIL_PASSWORD')
        self.RECEIVE_EMAIL = os.getenv('RECEIVE_EMAIL')

    def send_message(self, depart_city, dest_city, flight_info):
        price = flight_info[0]
        departure_city = depart_city
        departure_airport = flight_info[1]
        destination_city = dest_city
        destination_airport = flight_info[2]
        departure_date = flight_info[3]
        return_date = flight_info[4]
        airline = flight_info[5]
        flight_dep = flight_info[6]
        flight_ret = flight_info[7]

        # Note: The text notification section of code no longer works as Twilio no longer offers a free tier.

        # twilio_client = Client(self.twilio_account_sid, self.twilio_auth_token)
        # message = twilio_client.messages \
        #     .create(
        #         body=f"Low price alert! Only ${price} to fly from {departure_city}-{departure_airport} "
        #         f"to {destination_city}-{destination_airport} from {departure_date} to {return_date} on {airline}.",
        #         from_="personal information removed",
        #         to="personal information removed"
        #     )
        #
        # print(message.status)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
            connection.login(user=self.MY_SEND_EMAIL, password=self.SEND_EMAIL_PASSWORD)
            connection.sendmail(
                from_addr=self.MY_SEND_EMAIL,
                to_addrs=self.RECEIVE_EMAIL,
                msg=f"Myrtle Beach Flight Prices!\n\n"
                    f"Low price alert! Only ${price} to fly from {departure_city}-{departure_airport} "
                    f"to {destination_city}-{destination_airport} from {departure_date} to {return_date} on {airline} "
                    f"departure flight {flight_dep} return flight {flight_ret}"
            )
