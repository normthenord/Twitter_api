import BotFuncs as Bot
import requests
import tweepy


def main():
    api = Bot.getAuth()
    screenname = "KingJames"
    # tweets = api.user_timeline(screenname, count=100, tweet_mode='extended')

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
    # Bot.startStream(api, "#HouseHunters")

    # # -----------------------------------------------
    # # Downloads by getting status from a user_timeline
    # Bot.downloadMediaFiles(tweets, screenname, False, False)
    # Bot.findDuplicateImages(screenname)

    # # ------------------------------------------------
    # # Downloads from a text file made by startStream()
    # # Expects (api, string, allowRetweet, allowVideo)
    # Bot.downloadMediaFilesFromTxtDoc(api, 'Disney', False, True)

    # # -------------------------------------------------
    # # Downloads mediafiles from search term in last 100 * count
    Bot.downloadMediaFilesSearch(api, "#Butts", 100, False, False)


if __name__ == "__main__":
    main()
