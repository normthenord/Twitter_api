import BotFuncs as Bot


def main():
    api = Bot.getAuth()
    screenname = "NateSilver538"
    tweets = api.user_timeline(screenname, count=100, tweet_mode='extended')

    # # --------------------------------------------
    # Bot.tweetAndReplyInBinary(api, "This robot needs sleep")

    # # -----------------------------------------------
    # Bot.postTweetRobot(api, "I test you")

    # # -----------------------------------------------
    # Bot.replyInBinary(api, tweets, screenname)

    # # -----------------------------------------------
    # Bot.postBinaryTweets(api, "I'm a binary boy")

    # # -----------------------------------------------
    # Bot.printTweets(tweets)

    # # -----------------------------------------------
    # Bot.textFileStatuses(api, tweets, screenname)

    # # -----------------------------------------------
    Bot.startStream(api, "#CodingTrain")

    # # -----------------------------------------------
    # # Downloads by getting status from a user_timeline
    # Bot.downloadMediaFilesFromTimeline(tweets, screenname)
    # Bot.findDuplicateImages(f'u_{screenname}')

    # # ------------------------------------------------
    # # Downloads from a text file made by startStream()
    # Bot.downloadMediaFilesFromTxtDoc(api, '#HollowKnight', False)


if __name__ == "__main__":
    main()
