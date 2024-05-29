# Crypto Meme Coin Predictive Analysis

## Introduction

This project aims to build a predictive analysis model for a crypto meme coin, leveraging historical price data, market indicators, and sentiment analysis. By utilizing various data science and machine learning techniques, this model will forecast future price movements, providing valuable insights for traders and enthusiasts.

## Project Overview

1. **Data Collection**: Gather historical price data, market indicators, and sentiment data from various sources.
2. **Data Preprocessing**: Clean, normalize, and engineer features from the collected data.
3. **Exploratory Data Analysis (EDA)**: Visualize data to understand trends and correlations.
4. **Model Building**: Develop and train predictive models using machine learning algorithms.
5. **Model Evaluation**: Assess model performance using appropriate metrics.
6. **Advanced Modeling** (Optional): Implement advanced techniques such as deep learning and sentiment analysis.
7. **Model Deployment**: Deploy the model as a web service for real-time predictions. (Future Improvement)

## Project Structure

- `data/`: Contains raw and processed data files.
- `notebooks/`: Jupyter notebooks for data analysis, model building, and evaluation.
- `scripts/`: Python scripts for data collection, preprocessing, and model training.
- `models/`: Saved models and related files.
- `api/`: Code for deploying the model as a web service.
- `README.md`: Project documentation and instructions.

### Tools and libraries used

- Python 3.7+
- Anaconda
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- TensorFlow/Keras
- BeautifulSoup4
- Tweepy


## Getting Started

### CoinGecko Data Fetcher 
This script fetches market data for any coin Id in CoinGecko.
It retrieves historical price data for the days you select up to 365 days and stores it in a Pandas DataFrame.

Usage Examples

Here are some example commands for using the script to fetch cryptocurrency data and save it to a CSV file:

1. **Fetch Bitcoin data in USD for the past 30 days and save it to a CSV file named `bitcoin_30_days.csv`:**
   ```sh
   python3 coingecko_data.py bitcoin usd 30 bitcoin_30_days.csv
2. **Fetch Ethereum data in USD for the past 365 days and save it to a CSV file named ethereum_365_days.csv:**
   ```sh 
   python3 coingecko_data.py ethereum usd 365 ethereum_365_days.csv
3. **Fetch Dogecoin data in USD for the past 7 days and save it to a CSV file named dogecoin_7_days.csv:**
   ```sh 
   python3 coingecko_data.py dogecoin usd 7 dogecoin_7_days.csv
4. **Fetch Litecoin data in EUR for the past 90 days and save it to a CSV file named litecoin_90_days.csv:**
   ```sh 
   python3 coingecko_data.py litecoin eur 90 litecoin_90_days.csv

These commands allow you to specify the cryptocurrency (coin_id), the currency to compare against (vs_currency), the number of days of historical data (days), and the output filename (output_filename).

### Twitter Data Fetcher 
Script is written to fetch tweets based on a coin specified by the user. Script was not tested due to X developer free account permissions. 

### Reddit Data Fetcher 
Currently on the waitlist for reddit developer account. 


