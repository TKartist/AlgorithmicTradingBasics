from DataCollector import DataCollector
from datetime import datetime
import pandas as pd
import pytz
import json

def main():
    start = datetime(2025, 4, 22, 9, 0, 0)
    end = datetime(2025, 5, 20, 9, 0, 0)
    dataCollector = DataCollector()
    dataCollector.collect_historical_data(start, end, "BTCUSDT", "1m")
    df = dataCollector.get_data_df()
    df.to_csv("bar_info.csv", index=False)
    

if __name__ == "__main__":
    main()