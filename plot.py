import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import ta

# Define the ticker symbol for EUR/INR
ticker_symbol = "EURINR=X"

# Specify the start and end dates
start_date = "2023-01-01"
end_date = "2024-02-16"

# Retrieve the currency data
currency_data = yf.download(ticker_symbol, start=start_date, end=end_date)
currency_data.to_csv('currency_data.csv')

# Calculate Moving Averages (MA)
currency_data['ma_short'] = ta.trend.sma_indicator(currency_data['Close'], window=20)
currency_data['ma_long'] = ta.trend.sma_indicator(currency_data['Close'], window=50)

# Calculate Bollinger Bands
bb_bands = ta.volatility.BollingerBands(currency_data['Close'], window=20)
currency_data['bb_upper'] = bb_bands.bollinger_hband()
currency_data['bb_middle'] = bb_bands.bollinger_mavg()
currency_data['bb_lower'] = bb_bands.bollinger_lband()

# Calculate CCI
currency_data['cci'] = ta.trend.cci(currency_data['High'], currency_data['Low'], currency_data['Close'], window=20)

# Plotting
plt.figure(figsize=(14, 7))

# Price chart
plt.plot(currency_data['Close'], label='Close Price', color='blue')
plt.plot(currency_data['ma_short'], label='20-Day MA', color='red')
plt.plot(currency_data['ma_long'], label='50-Day MA', color='green')
plt.title('EUR/INR Price Chart with Moving Averages and CCI')
plt.xlabel('Date')
plt.ylabel('Price (INR)')
plt.legend()

# CCI plot
plt.figure(figsize=(14, 3))
plt.plot(currency_data['cci'], label='CCI', color='purple')
plt.title('Commodity Channel Index (CCI)')
plt.xlabel('Date')
plt.ylabel('CCI')
plt.legend()

plt.tight_layout()
plt.show()

# Calculate Bollinger Bands
bb_indicator = ta.volatility.BollingerBands(currency_data['Close'], window=20)
upper_band = bb_indicator.bollinger_hband()
middle_band = bb_indicator.bollinger_mavg()
lower_band = bb_indicator.bollinger_lband()

# Plotting
plt.figure(figsize=(14, 10))

# Close Price plot
plt.subplot(3, 1, 1)
plt.plot(currency_data['Close'], label='Close Price', color='blue')
plt.title('EUR/INR Price')
plt.xlabel('Date')
plt.ylabel('Price (INR)')
plt.legend()

# Upper Bollinger Band plot
plt.subplot(3, 1, 2)
plt.plot(upper_band, label='Upper Band', color='red')
plt.title('Bollinger Bands')
plt.xlabel('Date')
plt.ylabel('Price (INR)')
plt.legend()

# Lower Bollinger Band plot
plt.subplot(3, 1, 3)
plt.plot(lower_band, label='Lower Band', color='green')
plt.title('Bollinger Bands')
plt.xlabel('Date')
plt.ylabel('Price (INR)')
plt.legend()

plt.tight_layout()
plt.show()  