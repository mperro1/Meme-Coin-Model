"""
Twitter Data Fetcher
====================
This script fetches tweets from Twitter using the Twitter API v2.
It authenticates using a Bearer Token and fetches tweets containing
a specific hashtag, storing them in a Pandas DataFrame.

Usage:
- Replace 'bearer_token' with your actual Bearer Token from the Twitter Developer Portal.
- Run the script to fetch tweets containing the specified hashtag.

Example:
    To fetch tweets containing the hashtag '#Bonk':
    python twitter_data.py
    python3 twitter_data.py

Note: Was unable to use due to X free developer account limitations
"""

import tweepy
import pandas as pd

# Twitter API keys and access tokens that you get from the Twitter Developer Portal
bearer_token = 'AAAAAAAAAAAAAAAAAAAAALMbuAEAAAAA2tJPTBX0KXdrNeNITlps1FHTZAI%3DejIVOcnrL7ibZmlfRpicIIMlm8gDPHRO4rfzhlCTI2CMewqRf6'

# Authenticating to Twitter using the provided credentials
def authenticate_twitter_app(bearer_token):
    client = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)
    return client

# Function to fetch tweets based on a query
def fetch_tweets(client, query, max_results=100):
    tweets = client.search_recent_tweets(query=query, tweet_fields=['created_at', 'text'], max_results=max_results)
    # Creates a list of tweets with their creation time and text
    tweet_list = [[tweet.created_at, tweet.text] for tweet in tweets.data]
    # Creates a DataFrame from the list of tweets
    df = pd.DataFrame(tweet_list, columns=['timestamp', 'tweet'])
    # Converts the 'timestamp' column to datetime format and extract the date
    df['date'] = pd.to_datetime(df['timestamp']).dt.date
    # Sets the 'date' column as the index of the DataFrame
    df.set_index('date', inplace=True)
    return df

def main():
    # Authenticating to Twitter 
    api = authenticate_twitter_app(bearer_token)
    # Fetching tweets containing the hashtag "#Bonk", with a limit of tweets
    tweet_df = fetch_tweets(api, '#Bonk', max_results=10)
    print(tweet_df.head())

if __name__ == "__main__":
    main()
