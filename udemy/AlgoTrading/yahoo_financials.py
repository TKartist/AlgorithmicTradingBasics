from yahoofinancials import YahooFinancials

ticker = "MSFT"
yahoo_financials = YahooFinancials(ticker)  # object
data = yahoo_financials.get_historical_price_data("2018-04-24", "2020-04-04", "daily")
# this library doesn't go deeper than daily, no intraday data.

# print(data)  # -> outputs JSON
