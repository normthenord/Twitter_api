from TwitterBotFunctions import *


def main():
    api = getAuth()
    screenname = "NormZBot"
    tweets = api.user_timeline(screenname, count=1, tweet_mode='extended')

    # # --------------------------------------------
    # tweetAndReplyInBinary(api, "Is pumpkin pie a lubricant?")

    postTweetRobot(api, "I test you")

    # replyInBinary(api, tweets, screenname)

    # postBinaryTweets(api, "I'm a binary boy")

    # printTweets(tweets)

    # textFileStatuses(api, tweets, screenname)


main()
