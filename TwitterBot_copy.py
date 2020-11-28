import settings
import tweepy
import os

consumer_key = os.getenv("TWITTER_API_KEY")
consumer_secret = os.getenv("TWITTER_API_SECRET")
access_token_key = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)

screenname = 'NormZBot'
tweets = api.user_timeline(screenname, count=200, tweet_mode='extended')


filename = f"Twitter_api\\txtFiles\\{screenname}.txt"


with open(filename, 'w', encoding='utf-8') as f:
    for tweet in tweets:
        full_text_retweeted = tweet._json.get("retweeted_status")
        if None != full_text_retweeted:
            f.write(str(tweet.created_at) + '\n' +
                    str(full_text_retweeted.get("full_text")) + '\nID: ' + str(tweet.id))
        else:
            f.write(str(tweet._json["full_text"]))
        f.write("\n-----------------------\n")

f.close()
