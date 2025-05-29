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


def categorize(x):
    if x > 80:
        return "high"
    elif x > 60:
        return "good"
    elif x > 40:
        return "neutral"
    elif x > 20:
        return "neutral"
    return "low"

color_map = {
    'low': 'blue',
    'mid' : 'yellow',
    'neutral': 'orange',
    'good' : 'black',
    'high': 'green'
}


df = pd.read_csv("bar_info.csv")

rsi = calculate_rsi(df["close"])
df["rsi_val"] = rsi
df["rsi_val"] = df["rsi_val"].map(categorize)
df = df[:100]
print(len(df))

colors = df["rsi_val"].map(color_map)
print(df.index)

plt.plot(df["open_time"], df['close'], color='gray', linestyle='-', marker='o')

# Recolor markers individually
for i in range(len(df)):
    plt.plot(df["open_time"][i], df['close'][i], marker='o', color=colors[i], markersize=8)
plt.title("Bar Chart with Color Mapping")
plt.xticks(rotation=90)
plt.savefig("rsi_mapped_prices.png", dpi=500)
df.to_csv("bar_info3.csv")
