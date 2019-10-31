import tweepy
import time
from ProjectKeys import consumer_key,consumer_secret,access_token,access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
# user = api.me()

# print(user.name)
# print(user.screen_name)
# print(user.followers_count)

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)

mySearch = 'Python developer'
numbersOfTweets = 2

for tweet in tweepy.Cursor(api.search, mySearch).items(numbersOfTweets):
    try:
        # tweet.favorite()
        print(tweet.text)
        print('Liked the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break




# genrous Bot
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     if follower.name == 'Meriel J':
#         follower.follow()
#         print('followed')
#         break
#     print(follower.name)


