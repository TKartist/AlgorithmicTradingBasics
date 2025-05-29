import pandas as pd
import requests
from datetime import datetime
import time


class DataCollector:

    def __init__(self):
        self.base_url = "https://api.binance.com/api/v3/klines"
        self.limit = 1000
        self.call_points = []
        self.params = {}
        self.data = []
        self.columns = ["open_time", "open", "close", "high", "low", "close", "vol", "close_time", "quote_volume", "trade_count", "taker_buy_base_asset_volume", "taker_buy_quote_asset_volume"]

    def run_spot_api_calls(self):
        for i in range(len(self.call_points) - 1):
            print(f"sending request {i}")
            self.params["startTime"] = self.call_points[i]
            self.params["endTime"] = self.call_points[i+1]
            response = requests.get(self.base_url, params=self.params)
            
            if response.status_code == 200:
                self.data += response.json()
            else:
                print(f"{response.status_code} : {response.text}")
            
            time.sleep(0.05)


    def collect_historical_data(self, start, end, symbol, frame):
        start_ms = int(start.timestamp() * 1000)
        end_ms = int(end.timestamp() * 1000)
        self.params = {
            "symbol" : symbol,
            "interval" : frame
        }
        while start_ms < end_ms:
            self.call_points.append(start_ms)
            start_ms += 60000000
        self.call_points.append(end_ms)
        self.run_spot_api_calls()


    def calculate_rsi(self, prices, period=14):
        delta = prices.diff()

        gain = delta.clip(lower=0)
        loss = -delta.clip(upper=0)

        avg_gain = gain.ewm(alpha=1/period, min_periods=period, adjust=False).mean()
        avg_loss = loss.ewm(alpha=1/period, min_periods=period, adjust=False).mean()

        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))

        return rsi

    def calculate_atr(self, df, period=14):
        high = df['High']
        low = df['Low']
        close = df['Close']

        tr = pd.concat([
            high - low,
            (high - close.shift()).abs(),
            (low - close.shift()).abs()
        ], axis=1).max(axis=1)

        atr = tr.ewm(alpha=1/period, min_periods=period, adjust=False).mean()
        
        return atr


    def get_data_df(self):
        df = pd.DataFrame(self.data, columns=self.columns)
        rsi = self.calculate_rsi(df["close"])
        df["rsi"] = rsi
        df["atr"] = self.calculate_atr(df)
        df.to_csv("bar_info.csv", index=False)
        return df


        
