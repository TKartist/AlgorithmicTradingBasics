import pandas as pd
from scipy.stats import gaussian_kde
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("bar_info_transformed.csv", index_col="open_time")


'''
realistically, trading during the asian exchange active hours will be beneficial due to less involvement from
institutional traders and more abundance of retail traders with aggressive sentiment based strategies.
It should have more readable and predictable price and volume movements
'''

def transform_data(df):
    print("GOOD")
    upper_thres = df[["open", "close"]].max(axis=1)
    lower_thres = df[["open", "close"]].min(axis=1)
    true_range = df["close"] - df["open"]
    tail = ((lower_thres - df["low"]) / df["low"]) * 100
    head = ((df["high"] - upper_thres) / df["low"]) * 100
    true_range_pct = (true_range / df["open"]) * 100

    data = {
        "body" : true_range_pct,
        "head" : head,
        "tail" : tail,
    }
    print("GOT HERE")
    return data


print(f"maximum head pct: {df['head'].max()}")
print(f"minimum head pct: {df['head'].min()}")
print(f"maximum tail pct: {df['tail'].max()}")
print(f"minimum tail pct: {df['tail'].min()}")
print(f"maximum body pct: {df['body'].max()}")
print(f"minimum body pct: {df['body'].min()}")
