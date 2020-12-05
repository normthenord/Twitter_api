import BotFuncs as Bot


def main():
    api = Bot.getAuth()
    screenname = "shiffman"
    tweets = api.user_timeline(screenname, count=100, tweet_mode='extended')

    # # --------------------------------------------
    # Bot.tweetAndReplyInBinary(api, "This robot needs sleep")

    # Bot.postTweetRobot(api, "I test you")

    # Bot.replyInBinary(api, tweets, screenname)

    # Bot.postBinaryTweets(api, "I'm a binary boy")

    # Bot.printTweets(tweets)

    # Bot.textFileStatuses(api, tweets, screenname)

    # # -----------------------------------------------
    # Bot.startStream(api, "#HollowKnight")

    # # -----------------------------------------------
    Bot.downloadMediaFiles(tweets, screenname)


if __name__ == "__main__":
    main()
