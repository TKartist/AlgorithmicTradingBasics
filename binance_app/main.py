from DataCollector import DataCollector
from datetime import datetime
import pandas as pd
import pytz
import json

def main():
    start = datetime(2017, 10, 1, 0, 0, 0)
    end = datetime(2025, 5, 22, 17, 0, 0)
    dataCollector = DataCollector()
    dataCollector.collect_historical_data(start, end, "BTCUSDT", "1m")
    dataCollector.get_data_df()
    

if __name__ == "__main__":
    main()