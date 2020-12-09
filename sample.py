import numpy as np
import pandas as pd
import requests
import math
import config

stocks = pd.read_csv('sp_500_stocks.csv')

# Testing the API
symbol = "AAPL"
api_url = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&interval=15min&slice=year1month1&apikey={config.api_key}"
# print(api_url)

# Format API HTTP GET response as JSON object
data = requests.get(api_url).json()
print(data)

# Variables to add to PD dataframe
price = data['50DayMovingAverage']
market_cap = int(data['MarketCapitalization'])/1000000000
pe_ratio = data["PERatio"]
print(symbol, price, market_cap, pe_ratio)

# Create PD dataframe
my_columns = ["Ticker", "Stock Price", "Market Cap($bn)", "ForwardPE"]
output_dataframe = pd.DataFrame(columns=my_columns)
output_dataframe.append(
    pd.Series(
        [
            symbol,
            price,
            market_cap,
            pe_ratio
        ],
        index=my_columns
    ),
    ignore_index=True
)
print(output_dataframe)
