import settings
import tweepy
import os
import random


consumer_key = os.getenv("TWITTER_API_KEY")
consumer_secret = os.getenv("TWITTER_API_SECRET")
access_token_key = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_TOKEN_SECRET")


def getAuth():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)
    api = tweepy.API(auth)
    return api


RobotSayingList = [" Beep", " Bop", " Boop"]


def postTweetRobot(apiObject, sayWhat):
    robotWords = ""
    randomNum = random.randint(2, len(RobotSayingList))
    for _ in range(randomNum):
        robotWords += RobotSayingList[random.randint(
            0, len(RobotSayingList)-1)]

    apiObject.update_status(sayWhat + robotWords)

    print(f"Tweeting: {sayWhat + robotWords}")


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


def printTweets(tweets):
    for tweet in tweets:
        print(tweet.text + '\n')


def main():
    api = getAuth()
    screenname = "NormZBot"
    tweets = api.user_timeline(screenname, count=1)

    replyInBinary(api, tweets, screenname)
    postBinaryTweets(api, "I'm a binary boy")
    postTweetRobot(api, "I'm a real boy! *screw nose extends*")
    printTweets(tweets)


main()
