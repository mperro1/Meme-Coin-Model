"""
CoinGecko Data Fetcher
=======================
This script fetches market data for Bitcoin from CoinGecko.
It retrieves historical price data for the past 365 days and stores it in a Pandas DataFrame.


Usage:
- Run the script to fetch Bitcoin market data from CoinGecko.
- The data will be printed as a Pandas DataFrame with the first few rows.

Example:
    python coingecko_data.py  <coin_id> <vs_currency> <days> <output_filename>
"""

import requests
import pandas as pd
import time
import sys

# Function to fetch data from CoinGecko
def fetch_data_from_coingecko(coin_id, vs_currency, days):
    url = f'https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart'
    params = {
        'vs_currency': vs_currency,
        'days': days
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 401:
        raise requests.exceptions.HTTPError(
            "401 Unauthorized: Check the API endpoint or authentication requirements."
        )
    elif response.status_code != 200:
        response.raise_for_status()
    
    data = response.json()
    prices = data['prices']
    
    return prices

# Function to process data into a DataFrame
def process_data(prices):
    df = pd.DataFrame(prices, columns=['timestamp', 'price'])
    df['date'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('date', inplace=True)
    df.drop('timestamp', axis=1, inplace=True)
    return df

# Function to save DataFrame to CSV
def save_to_csv(df, filename):
    df.to_csv(filename, index=True)

def main(coin_id, vs_currency, days, output_filename):
    # Fetch data from CoinGecko
    prices = fetch_data_from_coingecko(coin_id, vs_currency, days)
    # Process data into DataFrame
    df = process_data(prices)
    # Print first few rows of the DataFrame
    print(df.head())
    # Save DataFrame to CSV
    save_to_csv(df, output_filename)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python coingecko_data.py <coin_id> <vs_currency> <days> <output_filename>")
        sys.exit(1)
    
    coin_id = sys.argv[1]
    vs_currency = sys.argv[2]
    days = sys.argv[3]
    output_filename = sys.argv[4]
    
    main(coin_id, vs_currency, days, output_filename)
