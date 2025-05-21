import json
import pandas as pd
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime
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
        return StockHistoricalDataClient(api_key, api_secret)

    def wrap_request(self, symbols, start, end, frame):
        if frame == "h":
            tf = TimeFrame.Hour
        elif frame == "m":
            tf = TimeFrame.Minute
        elif frame == "d":
            tf = TimeFrame.Day
        else:
            return None
        
        request_params = StockBarsRequest(
            symbol_or_symbols=symbols,
            timeframe=TimeFrame.Minute,
            start=start,
            end=end
        )
        return request_params

    def collect_historical_data(self, request_params):
        try:
            bars = self.client.get_stock_bars(request_params)
            return bars
        except Exception as e:
            print(f"Error while pulling data from Alpaca: {e}")
