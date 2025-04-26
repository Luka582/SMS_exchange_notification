import requests
from twilio.rest import Client
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()

ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
MY_PHONE_NUMBER = os.getenv("MY_PHONE_NUMBER")
ABOVE_FRACTION = 0.005
CURRENCY = "nok"


def this_month_data(currency_symbol):
    thirty_days_prior_date = (datetime.now() - timedelta(days = 30)).strftime("%Y-%m-%d")
    response = requests.get(f"https://kurs.resenje.org/api/v1/currencies/{currency_symbol}/rates/{thirty_days_prior_date}/count/30")
    response.raise_for_status()
    return [x["exchange_buy"] for x in response.json()["rates"]]
    
    

def is_worth_converting(month_data):
    today = month_data[-1]
    week_average = sum(month_data[23:])/len(month_data[23:])
    month_average = sum(month_data)/len(month_data)
    if today >= max(week_average,month_average)*(1+ABOVE_FRACTION):
        return today
    return False
    

todays_price = is_worth_converting(this_month_data(CURRENCY))
if todays_price == False:
    quit()
client = Client(ACCOUNT_SID,AUTH_TOKEN)
message = client.messages \
    .create(
        body = f"Cena nije loša danas, 1 {CURRENCY} = {round(todays_price,2)} rsd",
        from_= TWILIO_PHONE_NUMBER,
        to = MY_PHONE_NUMBER
        
    )

print(message.status)


