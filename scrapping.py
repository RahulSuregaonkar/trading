import yfinance as yf
import pandas as pd

# Define the ticker symbol for EUR/INR
ticker_symbol = "EURINR=X"

# Specify the start and end dates
start_date = "2023-01-01"
end_date = "2024-02-16"

# Define a list to store dataframes
dfs = []

# Define interval size (e.g., one month)
interval = pd.DateOffset(months=1)

# Iterate over the specified period in intervals
current_date = pd.to_datetime(start_date)
while current_date < pd.to_datetime(end_date):
    # Define the end of the interval
    interval_end = min(current_date + interval, pd.to_datetime(end_date))
    
    # Retrieve data for the current interval
    currency_data = yf.download(ticker_symbol, start=current_date, end=interval_end)
    
    # Append data to the list of dataframes
    dfs.append(currency_data)
    
    # Update current date for the next iteration
    current_date = interval_end + pd.DateOffset(days=1)

# Concatenate dataframes
currency_data_combined = pd.concat(dfs)

# Export the combined data to a CSV file
csv_file_path = "currency_data_eur_inr_combined.csv"
currency_data_combined.to_csv(csv_file_path)

print("Combined currency data exported to:", csv_file_path)
