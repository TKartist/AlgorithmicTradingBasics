import pandas as pd
import yfinance as yf

symbol = "STRK22691-USD"

def request_data_yfinance():
    try:
        ticker = yf.Ticker(symbol)
        print("Duck")
        closing_prices = ticker.history(period='max', interval='1d')[["Close"]]
        closing_prices.index = pd.to_datetime(closing_prices.index.strftime("%Y-%m-%d"))

        print(closing_prices.head())
        closing_prices.to_csv("starknet_token_price.csv")
    except Exception as e:
        print(f"Error fetching data {e}")

request_data_yfinance()