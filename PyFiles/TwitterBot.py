import BotFuncs as Bot
import requests


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
<<<<<<< HEAD
    # Bot.startStream(api, "#OSRS")
=======
    Bot.startStream(api, "#HouseHunters")
>>>>>>> 818916ad5f695bbf41772a709b6f94e9f60c0594

    # # -----------------------------------------------
    # # Downloads by getting status from a user_timeline
    # Bot.downloadMediaFiles(tweets, screenname, False, False)
    # Bot.findDuplicateImages(screenname)

    # # ------------------------------------------------
    # # Downloads from a text file made by startStream()
    # # Expects (api, string, allowRetweet, allowVideo)
    # Bot.downloadMediaFilesFromTxtDoc(api, 'Disney', False, True)

    # # ------------------------------------------------
    # # Downloads last 100 media files by search term
    tweets = api.search("#HollowKnight",
                        count='500', tweet_mode='extended')
    Bot.downloadMediaFiles(tweets, '#HollowKnight2', False, False)


if __name__ == "__main__":
    main()
