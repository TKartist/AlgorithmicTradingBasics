import pandas as pd
from scipy.stats import gaussian_kde
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("bar_info.csv", index_col="open_time")

'''
realistically, trading during the asian exchange active hours will be beneficial due to less involvement from
institutional traders and more abundance of retail traders with aggressive sentiment based strategies.
It should have more readable and predictable price and volume movements
'''

def transform_data(df):
    print("GOOD")
    body = df["open"] - df["close"]
    upper_thres = df[["open", "close"]].max(axis=1)
    lower_thres = df[["open", "close"]].min(axis=1)
    true_range = df["close"] - df["open"]
    tail = (lower_thres - df["low"]) / true_range.abs()
    head = df["high"] - upper_thres / true_range.abs()
    true_range = true_range / df["open"]

    data = {
        "body" : body,
        "head" : head,
        "tail" : tail,
        "profit" : true_range,
    }
    print("GOT HERE")
    return data

x = transform_data(df[43200:])
df_t = pd.DataFrame(x)
df_t.to_csv("bar_info_transformed.csv")