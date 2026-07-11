import json
import os


FILE="sent_tweets.json"



def load():

    if not os.path.exists(FILE):
        return []


    with open(FILE,"r") as f:
        return json.load(f)



def exists(tweet_id):

    data=load()

    return tweet_id in data



def save(tweet_id):

    data=load()

    data.append(tweet_id)


    with open(FILE,"w") as f:
        json.dump(
            data,
            f
        )
