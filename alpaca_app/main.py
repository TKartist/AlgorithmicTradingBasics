from DataCollector import DataCollector
from datetime import datetime
import pandas as pd

def main():
    start = datetime(2024, 5, 1, 9, 0)
    end = datetime(2024, 5, 1, 16, 0)
    symbol = "AAPL"
    frame = "m"
    data_collector = DataCollector()

    request_params = data_collector.wrap_request(start, end, symbol, frame)
    print(request_params)
    bars = data_collector.collect_historical_data(request_params)
    data = []
    for bar in bars.data["AAPL"]:
        data.append({
            "timestamp" : bar.timestamp,
            "open" : bar.open,
            "close" : bar.close,
            "high" : bar.high,
            "low" : bar.low,
            "volume" : bar.volume
        })
    df = pd.DataFrame(data)
    df.to_csv("aapl_prices_1min.csv", index=False)
    print("Data collected")



if __name__ == "__main__":
    main()