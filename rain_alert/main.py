import requests
import os
from twilio.rest import Client
api_KEY = "api-key"
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
account_sid="acc_sid"
auth_token="token"
weather_params = {
    "lat": 59.334591,
    "lon": 18.063240,
    "appid": api_KEY,
    "exclude": "current,minutely,daily"
}
response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
data = response.json()
num = 0
will_rain=False
for _ in range(12):
    if data['hourly'][num]['weather'][0]['id'] < 700:
        will_rain=True

    num += 1
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Remember to bring an umbrella",
        from_='+1620xxxx',
        to='+46734xxxxx'
    )

    print(message.status)
