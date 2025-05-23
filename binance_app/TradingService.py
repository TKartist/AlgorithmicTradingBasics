import requests
import json
import pandas as pd
from alpaca.trading.client import TradingClient
import os
from dotenv import load_dotenv


class TradingService:
    def __init__(self):
        self._load_env()
        self.client = self._initiate_client()

    def _load_env(self):
        load_dotenv()

    def _initiate_client(self):
        api_key = os.getenv("API_KEY")
        api_secret = os.getenv("API_SECRET")
        if not api_key or not api_secret:
            raise ValueError("API_KEY and/or API_SECRET not set in environment.")
        return TradingClient(api_key, api_secret)

    def get_account_info(self):
        return self.client.get_account()

    def collect_historical_data(self, symbol, start, end, duration):
        print(f"Collecting historical data for {symbol} from {start} to {end} (duration: {duration})...")
        '''Implement historical data here lolski'''