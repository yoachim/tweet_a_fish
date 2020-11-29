import tweepy
from config import create_api

if __name__ == "__main__":
    api = create_api()
    api.update_status("Hello World! #HelloWorld")

