import os
import requests
from twilio.rest import Client

api_key = OWM_API
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
CNT_COUNT = 5

account_sid = TWILIO_SID
auth_token = TWILIO_AUTH
twilio_phone = TWILIO_WHATSAPP_NUMBER
my_phone = MY_WHATSAPP

parameters = {
    "lat": -9.442020,
    "lon": 159.950516,
    "cnt": CNT_COUNT,
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False

for entry in data["list"]:
    condition_code = entry["weather"][0]["id"]
    if int(condition_code) < 800:
        will_rain = True
    else:
        will_rain = False

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="whatsapp:twilio_phone",
        body="It's going to rain today. Remember to bring an umbrella",
        to="whatsapp:my_phone"
    )
