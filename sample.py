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
my_columns = ["Ticker", "Stock Price", "Market Cap($bn)", "Forward PE"]
output_dataframe = pd.DataFrame(columns=my_columns)
data_points = pd.Series(
    [symbol, price, market_cap, pe_ratio], index=my_columns)
final_dataframe = output_dataframe.append(data_points, ignore_index=True)
print(final_dataframe)

output_dataframe = pd.DataFrame(columns=my_columns)
for ticker in stocks["Ticker"][:5]:
    api_url = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={ticker}&interval=15min&slice=year1month1&apikey={config.api_key}"
    data = requests.get(api_url).json()
    data_points = pd.Series(
        [ticker, data['50DayMovingAverage'], data['MarketCapitalization'], data["PERatio"]], index=my_columns)
    final_dataframe = output_dataframe.append(data_points, ignore_index=True)

print(final_dataframe)


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
    symbol_groups = list(chunks(stocks['Ticker'], 100))
    symbol_strings = []
    for i in range(0, len(symbol_groups)):
        symbol_strings.append(','.join(symbol_groups[i]))
    #     print(symbol_strings[i])
    my_columns = ['Ticker', 'Price',
                  'One-Year Price Return', 'Number of Shares to Buy']


symbol_groups = list(chunks(stocks['Ticker'], 100))
symbol_strings = []
for i in range(0, len(symbol_groups)):
    symbol_strings.append(','.join(symbol_groups[i]))
#     print(symbol_strings[i])

final_dataframe = pd.DataFrame(columns=my_columns)

for symbol_string in symbol_strings:
    #     print(symbol_strings)
    batch_api_call_url = f"https://www.alphavantage.co/batch/query?function=OVERVIEW&symbol={symbol}&interval=15min&slice=year1month1&apikey={config.api_key}"
    data = requests.get(batch_api_call_url).json()
