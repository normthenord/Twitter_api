import BotFuncs as Bot
import requests


def main():
    api = Bot.getAuth()
    screenname = "shiffman"
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
    # Bot.startStream(api, "#")

    # # -----------------------------------------------
    # # Downloads by getting status from a user_timeline
    # Bot.downloadMediaFilesFromTimeline(tweets, screenname)
    # Bot.findDuplicateImages(screenname)

    # # ------------------------------------------------
    # # Downloads from a text file made by startStream()
    Bot.downloadMediaFilesFromTxtDoc(api, 'Disney', False, True)


if __name__ == "__main__":
    main()
