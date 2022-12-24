import yfinance as yf
import matplotlib.pyplot as plt

# Collect stock data for a single stock
ticker = "AAPL"
stock_data = yf.Ticker(ticker).history(period="1y")

# Clean and prepare the data
stock_data.dropna(inplace=True)
stock_data["return"] = stock_data["Close"].pct_change()

# Calculate the moving average
stock_data["ma"] = stock_data["Close"].rolling(window=10).mean()

# Visualize the results
plt.plot(stock_data["Close"], label="Close")
plt.plot(stock_data["ma"], label="Moving Average")
plt.legend()
plt.show()