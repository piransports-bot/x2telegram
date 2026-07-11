import json
import os


FILE="sent.json"



def is_sent(tweet_id):

    if not os.path.exists(FILE):
        return False


    with open(FILE) as f:
        data=json.load(f)


    return tweet_id in data



def save(tweet_id):

    if os.path.exists(FILE):

        with open(FILE) as f:
            data=json.load(f)

    else:
        data=[]


    data.append(tweet_id)


    with open(FILE,"w") as f:
        json.dump(
            data,
            f
        )
