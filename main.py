
import requests
from pyexpat.errors import messages
from twilio.rest import Client

api_key="f79309b2b63d06b61ac426d233374577"
OWM_Endpoint="https://api.openweathermap.org/data/2.5/forecast"
account_sid="AC7c357bb2c7078979800071781270f39"
auth_token="0549b1242150c7722300012423d23239f1"
weather_params={
    "lat":43.731548,
    "lon":-79.762421,
    "appid":api_key,
    "cnt":4
}
response=requests.get(OWM_Endpoint,params=weather_params)
response.raise_for_status()
data=response.json()["list"]
j={}
will_rain=False
for i in data:
    j=i["weather"][0]
    if int(j["id"])<700:
        will_rain=True

if will_rain:
    client=Client(account_sid, auth_token)
    message=client.messages \
    .create(
        body="It may rain, bring an umbrella.",
        from='+15190000000',
        to='+15190000000'
    )
