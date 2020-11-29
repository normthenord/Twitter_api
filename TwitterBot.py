import settings
import tweepy
import os
import random
import time

consumer_key = os.getenv("TWITTER_API_KEY")
consumer_secret = os.getenv("TWITTER_API_SECRET")
access_token_key = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_TOKEN_SECRET")


def getAuth():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)
    api = tweepy.API(auth)
    return api


RobotSayingList = [" Beep", " Boop"]


def postTweetRobot(apiObject, sayWhat):
    robotWords = ""
    randomNum = random.randint(2, 4)
    for _ in range(randomNum):
        robotWords += RobotSayingList[random.randint(
            0, len(RobotSayingList)-1)]
    print(f"Tweeting: {sayWhat + robotWords}")
    return apiObject.update_status(sayWhat + robotWords)


def postBinaryTweets(apiObject, sayWhat):
    tweetBinary = "".join(format(ord(i), 'b') for i in sayWhat)
    apiObject.update_status(tweetBinary)


def replyInBinary(apiObject, tweets, screenname):  # Reply to last tweet in binary
    for tweet in tweets:
        id = tweet.id
        origText = tweet.text
        binaryText = "".join(format(ord(i), 'b') for i in origText)
        if len(binaryText + f"@{screenname}") > 280:
            apiObject.update_status(
                f'@{screenname} ' + binaryText[:265] + '...', id)

        else:
            apiObject.update_status(f'@{screenname} ' + binaryText, id)


def replyInBinaryToId(apiObject, TweetId):
    id = TweetId
    tweet = apiObject.get_status(id)
    origText = tweet.text
    screenname = tweet.user.screen_name
    binaryText = "".join(format(ord(i), 'b') for i in origText)
    if len(binaryText + f"@{screenname}") > 280:
        apiObject.update_status(
            f'@{screenname} ' + binaryText[:265] + '...', id)
    else:
        apiObject.update_status(f'@{screenname} ' + binaryText, id)


def printTweets(tweets):
    for tweet in tweets:
        print(tweet.text + '\n')


def tweetAndReplyInBinary(apiObject, tweetString):
    My_Tweet = My_Tweet = postTweetRobot(apiObject, tweetString)
    replyInBinaryToId(apiObject, My_Tweet.id)


def textFileStatuses(apiObject, screenname):
    tweets = apiObject.user_timeline(
        screenname, count=200, tweet_mode='extended')

    filename = f"C:\\Users\\xstom\\OneDrive\\Desktop\\Python Challenge\\Twitter_api\\txtFiles\\{screenname}.txt"

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


def main():
    api = getAuth()
    screenname = "NormZBot"
    tweets = api.user_timeline(screenname, count=1)

    # # --------------------------------------------
    # tweetAndReplyInBinary(api, "Hello, one and all")

    # postTweetRobot("Hello, little lady")

    # replyInBinary(api, tweets, screenname)

    # postBinaryTweets(api, "I'm a binary boy")

    printTweets(tweets)

    # textFileStatuses(api, screenname)


main()
