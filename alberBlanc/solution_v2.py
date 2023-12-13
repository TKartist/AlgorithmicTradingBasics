import pandas as pd
import numpy as np


class TradingStrategy:
    def _init_(
        self,
        short_window=40,
        long_window=100,
        rsi_period=14,
        atr_period=14,
        rsi_overbought=70,
        rsi_oversold=30,
        atr_threshhold=2,
    ):
        self.short_window = short_window
        self.long_window = long_window
        self.rsi_period = rsi_period
        self.atr_period = atr_period
        self.rsi_overbought = rsi_overbought
        self.rsi_oversold = rsi_oversold
        self.atr_threshhold = atr_threshhold
        self.bought_positions = []
        self.total_profit = 0
        self.data = pd.DataFrame(
            columns=["timestamp", "price", "quantity", "high", "low", "close"]
        )

    def calculate_rsi(self, series, period):
        delta = series.diff().dropna()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    def calculate_atr(self, df, period):
        high_low = df["high"] - df["low"]
        high_close = np.abs(df["high"] - df["close"].shift())
        low_close = np.abs(df["low"] - df["close"].shift())
        ranges = pd.concat([high_low, high_close, low_close], axis=1)
        true_range = np.max(ranges, axis=1)
        atr = true_range.rolling(window=period).mean()
        return atr

    def process_transaction(self, row):
        self.data = self.data.append(row, ignore_index=True)
        if self.data.shape[0] >= self.long_window:
            self.data["short_mavg"] = (
                self.data["price"]
                .rolling(window=self.short_window, min_periods=1)
                .mean()
            )
            self.data["long_mavg"] = (
                self.data["price"]
                .rolling(window=self.long_window, min_periods=1)
                .mean()
            )
            self.data["rsi"] = self.calculate_rsi(self.data["price"], self.rsi_period)
            self.data["atr"] = self.calculate_atr(self.data, self.atr_period)

            # Implement buy or sell logic
            latest_data = self.data.iloc[-1]
            if self.should_buy(latest_data):
                self.buy(latest_data["price"], abs(latest_data["quantity"]))
            elif self.should_sell(latest_data):
                self.sell(latest_data["price"], abs(latest_data["quantity"]))

    def should_buy(self, latest_data):
        if (
            latest_data["short_mavg"] > latest_data["long_mavg"]
            and latest_data["rsi"] < self.rsi_oversold
        ):
            if latest_data["atr"] < self.atr_threshhold:  # Define your ATR threshold
                return True
        return False

    def should_sell(self, latest_data):
        if (
            latest_data["short_mavg"] < latest_data["long_mavg"]
            and latest_data["rsi"] > self.rsi_overbought
        ):
            if latest_data["atr"] < self.atr_threshhold:  # Define your ATR threshold
                return True
        return False

    def buy(self, price, quantity):
        self.bought_positions.append((price, quantity))

    def sell(self, price, quantity):
        remaining_quantity = quantity
        while remaining_quantity > 0 and self.bought_positions:
            buy_price, buy_quantity = self.bought_positions.pop(0)
            sell_quantity = min(buy_quantity, remaining_quantity)
            profit = sell_quantity * (price - buy_price)
            self.total_profit += profit
            remaining_quantity -= sell_quantity

            if buy_quantity > sell_quantity:
                self.bought_positions.insert(
                    0, (buy_price, buy_quantity - sell_quantity)
                )


# Load data from CSV file
csv_file = "data_v2.csv"  # Replace with your CSV file path
data_stream = pd.read_csv(csv_file)

# Initialize and run strategy
strategy = TradingStrategy()
for _, row in data_stream.iterrows():
    strategy.process_transaction(row)

print(f"Total Profit: {strategy.total_profit}")
