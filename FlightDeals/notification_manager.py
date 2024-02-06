import os
from twilio.rest import Client

TWILIO_SID = os.environ.get("TWILIO_SID", "Twilio User not found")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN", "Twilio auth token not found")
MY_TWILIO_NUMBER = os.environ.get("MY_TWILIO_NUMBER", "Twilio number not found")
MY_NUMBER = os.environ.get("MY_NUMBER", "Delivery number not found")


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_notification(self, note):
        message = self.client.messages.create(
            body=note,
            from_=MY_TWILIO_NUMBER,
            to=MY_NUMBER
        )
        print(message.sid)
