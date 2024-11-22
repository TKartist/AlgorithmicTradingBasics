import pandas as pd
from data_collector import request_data_yfinance
import os
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np


def fourrier_transformation(df):
    df.index = pd.to_datetime(df.index)
    df["Days"] = (df.index - df.index.min()) / pd.Timedelta(days=1)

    fft_values = np.fft.fft(df["Close"])
    freq = np.fft.fftfreq(len(fft_values), d=1)
    power = np.abs(fft_values)

    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(df['Days'], df['Close'], label='Original Signal')
    plt.title('Original Time Series Signal')
    plt.xlabel('Days')
    plt.ylabel('Value')
    plt.legend()
    plt.grid()

    # Plot Power Spectrum
    plt.subplot(2, 1, 2)
    plt.plot(freq[:len(freq)//2], power[:len(power)//2], label='Power Spectrum', color='red')
    plt.title('Fourier Transform - Power Spectrum')
    plt.xlabel('Frequency (1/Days)')
    plt.ylabel('Power')
    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.savefig("fft_analysis.png")


def linear_regression_analysis(df):
    df.index = pd.to_datetime(df.index)
    df["Days"] = (df.index - df.index.min()) / pd.Timedelta(days=1)
    X = df["Days"].values.reshape(-1, 1)
    y = df["Close"]

    model = LinearRegression()
    model.fit(X, y)

    df["trend"] = model.predict(X)
    df[["Close", "trend"]].plot(legend=True)
    plt.savefig("linear_reg_analysis.png")


def rolling_mean_analysis(df, window_size=30):
    df["rolling_mean"] = df["Close"].rolling(window=window_size).mean()
    df.plot(legend=True)
    plt.savefig("rolling_mean.png")




def main():
    filenames = os.listdir(".")
    target = "starknet_token_price.csv"
    if target not in filenames:
        request_data_yfinance()

    df = pd.read_csv(target, index_col="Date")
    fourrier_transformation(df)

if __name__ == "__main__":
    main()