from urllib.request import urlopen
import certifi
import json
import pandas as pd
import requests

from VARIABLES import ONE_MIN_CANDLES

def get_jsonparsed_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for candle in data:
            print(candle)
    else:
        print("Failed to fetch data:", response.status_code, response.text)



def url_creator(type, params):
    root = f"https://financialmodelingprep.com/stable{type}"
    for key, val in params.items():
        root = f"{root}?{key}={val}&"
    return(root[:-1])


params = {
    "apikey" : "dnlwzHFGRUfWSDP1O4FLwSkzHRT3wYQC",
    "symbol" : "AAPL",
    "from" : "2024-01-01",
    "to" : "2024-03-01",
}

url = url_creator(ONE_MIN_CANDLES, params)
print(url)
apple_5_years = get_jsonparsed_data(url)
df = pd.DataFrame(apple_5_years)
df.to_csv("apple_five_years.csv")
