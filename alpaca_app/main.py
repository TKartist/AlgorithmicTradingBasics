from DataCollector import DataCollector
from datetime import datetime
import pandas as pd
import pytz
import json

def main():
    start = "2024-05-01"
    end = "2024-05-02"
    symbol = "BTC/USDT"
    frame = "1T"

    dataCollector = DataCollector()
    bars = dataCollector.collect_historical_data(start, end, symbol, frame)
    df = pd.DataFrame(bars["bars"][symbol])
    df.to_csv("bar_info.csv", index=False)


if __name__ == "__main__":
    main()