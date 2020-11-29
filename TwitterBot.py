import BotFuncs


def main():
    api = BotFuncs.getAuth()
    screenname = "NormZBot"
    tweets = api.user_timeline(screenname, count=1, tweet_mode='extended')

    # # --------------------------------------------
    # BotFuncs.tweetAndReplyInBinary(api, "Is pumpkin pie a lubricant?")

    BotFuncs.postTweetRobot(api, "I test you")

    # BotFuncs.replyInBinary(api, tweets, screenname)

    # BotFuncs.postBinaryTweets(api, "I'm a binary boy")

    # BotFuncs.printTweets(tweets)

    # BotFuncs.textFileStatuses(api, tweets, screenname)


if __name__ == "__main__":
    main()
