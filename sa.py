import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override() # <-- This line is needed to use Yahoo Finance as the data source

# Set the ticker and the start and end dates
ticker = "AUM"
start_date = " "
end_date = "YYYY-MM-DD"

# Use pandas-datareader to fetch the data
data = pdr.get_data_yahoo(ticker, start_date, end_date)

# Print the first five rows of the data
print(data.head())