import pandas as pd
from scipy.stats import gaussian_kde
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("bar_info.csv")

def transform_data(df):
    print("GOOD")
    body = df["open"] - df["close"]
    upper_thres = df[["open", "close"]].max(axis=1)
    lower_thres = df[["open", "close"]].min(axis=1)
    increase = df["open"] < df["close"]
    head = df["high"] - upper_thres
    tail = lower_thres - df["low"]

    data = {
        "body" : body,
        "head" : head,
        "tail" : tail,
        "profit" : increase,
    }
    print("GOT HERE")

transform_data(df)
