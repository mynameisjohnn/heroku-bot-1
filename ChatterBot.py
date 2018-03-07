# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "9sTkEMvUyvMgHU85BWo5uJJ5j"
consumer_secret = "26mCXtJ2br5GMadSTRDWcpGzDvKRsbv0GmzQinFum56Jenvuzg"
access_token = "969399907466452992-oyP9A4u7h2rWHnuxwnfaab5SaOROwYZ"
access_token_secret = "G14n0aroFpwJdIVZNlQd7w2f8LKjQ8AUqxettSUAgtwmR"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
# CODE GOES HERE