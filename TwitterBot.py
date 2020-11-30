import BotFuncs as Bot


def main():
    api = Bot.getAuth()
    screenname = "shiffman"
    tweets = api.user_timeline(screenname, count=10, tweet_mode='extended')

    # # --------------------------------------------
    # Bot.tweetAndReplyInBinary(api, "Is pumpkin pie a lubricant?")

    # Bot.postTweetRobot(api, "I test you")

    Bot.replyInBinary(api, tweets, screenname)

    # Bot.postBinaryTweets(api, "I'm a binary boy")

    # Bot.printTweets(tweets)

    # Bot.textFileStatuses(api, tweets, screenname)


if __name__ == "__main__":
    main()
