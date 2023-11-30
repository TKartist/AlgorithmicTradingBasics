# Alpha Vantage -> free data collection API, free 5 API calls a minute only

from AV_apiKey import api_key

# returns JSON data
# Full returns the full history
# compact returns top 100

from alpha_vantage.timeseries import TimeSeries
import pandas as pd

ts = TimeSeries(key=api_key, output_format="pandas")
data = ts.get_daily(symbol="EURUSD", outputsize="full")[0]

data.columns = ["open", "high", "low", "close", "volume"]

all_tickers = ["AAPL", "MSFT", "CSCO", "AMZN", "GOOG", "FB"]
close_price = pd.DataFrame()

for ticker in all_tickers:
    ts = TimeSeries(key=api_key, output_format="pandas")
    data = ts.get_intraday(symbol=ticker, interval="1min", outputsize="compact")[0]
    data.columns = ["open", "high", "low", "close", "volume"]
    close_price[ticker] = data["close"]
