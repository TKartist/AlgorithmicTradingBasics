import json
import pandas as pd
import requests
from datetime import datetime
import os
from dotenv import load_dotenv


class DataCollector:

    def __init__(self):
        self._load_env()
        self.headers = {
            "accept" : "application/json",
            "APCA-API-KEY-ID" : os.getenv("API_KEY"),
            "APCA-API-SECRET-KEY" : os.getenv("API_SECRET")
        }
        self.base_url = "https://data.alpaca.markets/v1beta3/crypto/us/bars"

    def _load_env(self):
        load_dotenv()

    def collect_recent_data(self, pagination_token):
        print("Collect recent data!!!")

    def collect_historical_data(self, start, end, symbols, frame):
        params = {
            "symbols" : symbols,
            "timeframe" : frame if frame else "1T",
            "start" : start if start else '2020-01-01',
            "end" : end if end else '2025-01-01'
        }

        response = requests.get(self.base_url, headers=self.headers, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None
