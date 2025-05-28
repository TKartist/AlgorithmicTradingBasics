import pandas as pd
import matplotlib.pyplot as plt

def calculate_rsi(prices, period=14):
    delta = prices.diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.ewm(alpha=1/period, min_periods=period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1/period, min_periods=period, adjust=False).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    return rsi


def calculate_atr(df, period=14):
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


def categorize(x):
    if x > 66:
        return "high"
    elif x < 34:
        return "low"
    return "neutral"

color_map = {
    'low': 'blue',
    'neutral': 'orange',
    'high': 'green'
}


df = pd.read_csv("bar_info.csv")

rsi = calculate_rsi(df["close"])
df["rsi_val"] = rsi
df["rsi_val"] = df["rsi_val"].map(categorize)
df.to_csv("bar_info3.csv")
