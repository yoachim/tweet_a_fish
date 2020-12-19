from os import environ
import tweepy


def create_api():
    # Authenticate to Twitter
    try:
        CONSUMER_KEY = environ['CONSUMER_KEY']
        CONSUMER_SECRET = environ['CONSUMER_SECRET']
        ACCESS_KEY = environ['ACCESS_KEY']
        ACCESS_SECRET = environ['ACCESS_SECRET']
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

        # Create API object
        api = tweepy.API(auth, wait_on_rate_limit=True,
                         wait_on_rate_limit_notify=True)
    # use the local file that isn't in the repo
    except KeyError:
        from config import create_api_local
        api = create_api_local()

    return api
