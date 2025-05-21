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

    def get_account_info(self):
        return self.client.get_account()

    def collect_historical_data_min(self, symbols, start, end):
        request_params = StockBarsRequest(
            symbol_or_symbols=symbols,
            timeframe=TimeFrame.Minute,
            start=start,
            end=end
        )

        bars = self.client.get_stock_bars(request_params)

        return bars

    def collect_historical_data_day(self, symbols, start, end):
        request_params = StockBarsRequest(
            symbol_or_symbols=symbols,
            timeframe=TimeFrame.Day,
            start=start,
            end=end
        )

        bars = self.client.get_stock_bars(request_params)

        return bars
    
    def collect_historical_data_hour(self, symbols, start, end):
        request_params = StockBarsRequest(
            symbol_or_symbols=symbols,
            timeframe=TimeFrame.Hour,
            start=start,
            end=end
        )

        bars = self.client.get_stock_bars(request_params)

        return bars