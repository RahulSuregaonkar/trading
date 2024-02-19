
import yfinance as yf
import pandas as pd
import ta

# Define the ticker symbol for EUR/INR
ticker_symbol = "EURINR=X"

# Specify the start and end dates
start_date = "2023-01-01"
end_date = "2024-02-23"  # Extended to cover one week beyond the specified date

# Retrieve the currency data
currency_data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Calculate Moving Averages (MA)
currency_data['ma_one_day'] = ta.trend.sma_indicator(currency_data['Close'], window=1)
currency_data['ma_one_week'] = ta.trend.sma_indicator(currency_data['Close'], window=5)

# Calculate Bollinger Bands
currency_data['bb_upper_one_day'], currency_data['bb_middle_one_day'], currency_data['bb_lower_one_day'] = ta.volatility.bollinger_hband_indicator(currency_data['Close'], window=1), ta.volatility.bollinger_mavg(currency_data['Close'], window=1), ta.volatility.bollinger_lband_indicator(currency_data['Close'], window=1)
currency_data['bb_upper_one_week'], currency_data['bb_middle_one_week'], currency_data['bb_lower_one_week'] = ta.volatility.bollinger_hband_indicator(currency_data['Close'], window=5), ta.volatility.bollinger_mavg(currency_data['Close'], window=5), ta.volatility.bollinger_lband_indicator(currency_data['Close'], window=5)

# Calculate Commodity Channel Index (CCI)
currency_data['cci_one_day'] = ta.trend.cci(currency_data['High'], currency_data['Low'], currency_data['Close'], window=1)
currency_data['cci_one_week'] = ta.trend.cci(currency_data['High'], currency_data['Low'], currency_data['Close'], window=5)

# Select the data for February 16, 2024
feb_16_2024_data = currency_data.loc['2024-02-16']

# Metrics for one day
ma_one_day_feb_16_2024 = feb_16_2024_data['ma_one_day']
bb_upper_one_day_feb_16_2024 = feb_16_2024_data['bb_upper_one_day']
bb_lower_one_day_feb_16_2024 = feb_16_2024_data['bb_lower_one_day']
cci_one_day_feb_16_2024 = feb_16_2024_data['cci_one_day']

# Metrics for one week
ma_one_week_feb_16_2024 = feb_16_2024_data['ma_one_week']
bb_upper_one_week_feb_16_2024 = feb_16_2024_data['bb_upper_one_week']
bb_lower_one_week_feb_16_2024 = feb_16_2024_data['bb_lower_one_week']
cci_one_week_feb_16_2024 = feb_16_2024_data['cci_one_week']

# Print the results
print("Metrics for one day (February 16, 2024):")
print("Moving Average (1 day):", ma_one_day_feb_16_2024)
print("Bollinger Bands (1 day): Upper:", bb_upper_one_day_feb_16_2024, "Lower:", bb_lower_one_day_feb_16_2024)
print("CCI (1 day):", cci_one_day_feb_16_2024)
print()
print("Metrics for one week (February 16, 2024):")
print("Moving Average (1 week):", ma_one_week_feb_16_2024)
print("Bollinger Bands (1 week): Upper:", bb_upper_one_week_feb_16_2024, "Lower:", bb_lower_one_week_feb_16_2024)
print("CCI (1 week):", cci_one_week_feb_16_2024)
