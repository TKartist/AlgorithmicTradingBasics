
import numpy as np
import pandas as pd  # panel datas -> pandas, it handles tabular data
import os

os.environ['IEX_SANDBOX'] = 'enable'

print("Pandas's version is:", pd.__version__)
# checking pandas version

import requests  # for http requests

print("Request's version is:", requests.__version__)
# checking requests version

import xlsxwriter as xls  # cells like excel
import math

# importing stock info (doesn't reflect real-time change as it is a paid function)
# save s&p500 csv file in pandas dataframe
stocks = pd.read_csv("sp_500_stocks.csv")
print(type(stocks))

# iex cloud api to gather all financial data
# we are going to use sandbox API and like most APIs we need some form of authentification to pull data from API
# This sandbox API usage exists for test purposes before using scripts IRL
# always put secrets.py in gitignore (for safety)
# we import API token
from Secrets import IEX_CLOUD_API_TOKEN

# API call for single stock (Apple in this case)

symbol = 'AAPL';
# all api have different formats and our IEX_CLOUD_API we use base url and depending on what we want, we can change the endpoint and get info we want
# we used fstring to append symbol to our url
api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token={IEX_CLOUD_API_TOKEN}'
#end point for stock price and market capitalization -> we use quote endpoint for both

print(api_url);
#example of fstring
adjective = "superb"
string = f"my life is {adjective}"
print(string);

# our first request
data = requests.get(api_url);
#to view the data
print(data.status_code);

