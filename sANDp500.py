import numpy as np
import pandas as pd  # panel datas -> pandas, it handles tabular data

print("Pandas's version is:", pd.__version__)
# checking pandas version

import requests as req  # for http requests

print("Request's version is:", req.__version__)
# checking requests version

import xlsxwriter as xls  # cells like excel
import math

# importing stock info (doesn't reflect real-time change as it is a paid function)
# save s&p500 csv file in pandas dataframe
stocks = pd.read_csv("sp_500_stocks.csv")
print(type(stocks))
