import yfinance as yf
import pandas as pd
import datetime as dt
from yahoo_financials import YahooFinancials

# ticker: initial indicating the company (stock basically)
# data = yf.download(
#     "MSFT", period="6mo"
# )
# downloads 6 month open high low close data of microsoft

# data = yf.download("MSFT", start="2017-01-01", end="2020-04-24")
# above downloads data from start to end date
# use date-time library to give start and end

data = yf.download("MSFT", period="1mo", interval="5m")
# how to get intraday (during the day) data (5 minute interval) in the last one month

stocks = [
    "AMZN",
    "MSFT",
    "INTC",
    "GOOG",
    "INFY.NS",  # indian company
    "3988.HK",  # Bank of China
]

# start = datetime.datetime.today() - datetime.timedelta(30)
# end = datetime.datetime.today()

# pandas DataFrame: very useful data structure
cl_price = pd.DataFrame()
ohlcv_data = {}  # dictionary


# for ticker in stocks:
#     cl_price[ticker] = yf.download(ticker, start, end)[
#         "Adj Close"
#     ]  # Adj Close : closingprice after adjustment of all applicable splits and dividends
#     # remove [] to get the whole dataset


# for ticker in stocks: #to print
#     print(cl_price[ticker])

# for ticker in stocks:
#     ohlcv_data[ticker] = yf.download(ticker, start, end)

# for ticker in stocks:
#     print(
#         ohlcv_data[ticker]["Open"]
#     )  # ->saved in format of a dictionary instead of pandas dataframe

# nan value-> due to holidays

# We also learn yahooFinancials, because libraries deprecate
# YahooFinancials uses web-scraper

close_prices = pd.DataFrame()
end_date = (dt.date.today()).strftime("%Y-%m-%d")
beg_date = (dt.date.today() - dt.timedelta(1825)).strftime("%Y-%m-%d")

### extracting JSON
for ticker in stocks:
    yahoo_financials = YahooFinancials(ticker)
    json_obj = yahoo_financials.get_historical_price_data(beg_date, end_date, "daily")
    ohlv = json_obj[ticker]["prices"]  # -> ohlv is a list of dictionaries
    temp = pd.DataFrame(ohlv)[
        ["formatted_date", "adjclose"]
    ]  # -> converts ohlv list of dicts into panda dataframe structure (more understandable), only taking formatted-date and adjusted close
    # technically it is a data parser (organizer(?))
    temp.set_index(
        "formatted_date", inplace=True
    )  # this sets "formatted_date" column as the index
    temp.dropna(
        inplace=True
    )  # removes NaN from the list -> it could be NaN if the dividends are given out that day
    close_prices[ticker] = temp[
        "adjclose"
    ]  # adds the adjusted close price of a company as a column of the data structure with date as index


print(
    close_prices["AMZN"]
)  # prints adjusted closing price of Amazon with date as index

print(
    close_prices["MSFT"]
)  # prints adjusted closing price of Amazon with date as index

print(
    close_prices["INTC"]
)  # prints adjusted closing price of Amazon with date as index

print(
    close_prices["GOOG"]
)  # prints adjusted closing price of Amazon with date as index
