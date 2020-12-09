import numpy as np
import pandas as pd
import requests
import math
import config

stocks = pd.read_csv('sp_500_stocks.csv')

symbol = "AAPL"
api_url = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&interval=15min&slice=year1month1&apikey={config.api_key}"
# print(api_url)

data = requests.get(api_url).json()
# print(data)

my_columns = ["Ticker", "Stock Price", "Market Cap", "ForwardPE"]
output_dataframe = pd.DataFrame(columns=my_columns)
print(output_dataframe)
