import tweepy
import os
import random
import settings
import requests

consumer_key = os.getenv("TWITTER_API_KEY")
consumer_secret = os.getenv("TWITTER_API_SECRET")
access_token_key = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_TOKEN_SECRET")

filter = ""


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        global filter
        # filter = '#HadesGame'
        filename = f'StreamTxtFiles\\{filter}'
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(status.created_at.strftime("%m/%d/%Y, %H:%M:%S") + '\n')
            if hasattr(status, "retweeted_status"):  # Check if Retweet
                try:
                    f.write("RT " +
                            status.retweeted_status.extended_tweet["full_text"])
                except AttributeError:
                    f.write("RT " + status.retweeted_status.text)
            else:
                try:
                    f.write(status.extended_tweet["full_text"])
                except AttributeError:
                    f.write(status.text)
            f.write('\nID: ' + status.id_str)
            f.write("\n-----------------------\n")


def startStream(apiObject, _filter):
    global filter
    filter = _filter
    myStreamListener = MyStreamListener()
    tweepy.Stream(auth=apiObject.auth,
                  listener=myStreamListener).filter(track=[filter], is_async=True)


def downloadMediaFiles(tweets, name):
    i = 1
    for tweet in tweets:
        if 'media' in tweet.entities:
            if not os.path.isdir(f'MediaFiles\\{name}'):
                os.mkdir(f'MediaFiles\\{name}')
            r = requests.get(tweet.entities['media'][0]['media_url'])
            while True:
                if os.path.isfile(f'MediaFiles\\{name}\\{name}_{i}.jpg'):
                    i += 1
                else:
                    with open(f'MediaFiles\\{name}\\{name}_{i}.jpg', 'wb') as f:
                        f.write(r.content)
                    break


def downloadMediaFilesFromTxtDoc(apiObject, name):
    with open(f'StreamTxtFiles\\{name}', 'r', encoding='utf-8') as f:
        ids = []
        splitText = f.read().split('\n')
        for line in splitText:
            if line.startswith("ID: "):
                ids.append(line[4:])

        id_list = []
        for i in range(int(len(ids)/100)+1):
            try:
                id_list.append(ids[i*100:(i+1)*100])
                print(len(id_list[i]))
            except:
                id_list.append(ids[i*100:])

        tweets = []
        for idz in id_list:
            if idz:
                print("Trying...")
                try:
                    tweets = apiObject.statuses_lookup(idz)
                except tweepy.TweepError as e:
                    print(e.args[0][0]['message'])
                    if e.args[0][0]['code'] == 88:
                        return
                downloadMediaFiles(tweets, name)


def getAuth():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)
    api = tweepy.API(auth)
    return api


def postTweetRobot(apiObject, sayWhat):
    RobotSayingList = [" Beep", " Boop"]
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
        if not tweet.full_text.startswith('RT'):
            id = tweet.id
            origText = tweet.full_text
            binaryText = "".join(format(ord(i), 'b') for i in origText)
            if len(binaryText + f"@{screenname}") > 280:
                post_text = f'@{screenname} ' + binaryText[:265] + '...'
                apiObject.update_status(post_text, id)
                print("Tweeting: " + post_text)

            else:
                post_text = f'@{screenname} ' + binaryText
                apiObject.update_status(post_text, id)
                print("Tweeting: " + post_text)
            return


def replyInBinaryToId(apiObject, TweetId):
    id = TweetId
    tweet = apiObject.get_status(id, tweet_mode='extended')
    origText = tweet.full_text
    screenname = tweet.user.screen_name
    binaryText = "".join(format(ord(i), 'b') for i in origText)
    if len(binaryText + f"@{screenname}") > 280:
        apiObject.update_status(
            f'@{screenname} ' + binaryText[:265] + '...', id)
        print("Tweeting: " + f'@{screenname} ' + binaryText[:265] + '...')
    else:
        apiObject.update_status(f'@{screenname} ' + binaryText, id)
        print("Tweeting: " + f'@{screenname} ' + binaryText)


def printTweets(tweets):
    for tweet in tweets:
        print(tweet.full_text + '\n')


def tweetAndReplyInBinary(apiObject, tweetString):
    My_Tweet = postTweetRobot(apiObject, tweetString)
    replyInBinaryToId(apiObject, My_Tweet.id)


def textFileStatuses(apiObject, tweets, screenname):

    filename = f"UserStatusTxtFiles\\{screenname}.txt"

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
    print(f"Done writing text in {screenname}.txt")
