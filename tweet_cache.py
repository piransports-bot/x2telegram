import os
import requests


WORKER_URL = os.getenv(
    "WORKER_URL"
)



def check_tweet(tweet_id):


    response = requests.post(
        WORKER_URL,
        json={
            "tweet_id": tweet_id
        },
        timeout=20
    )


    data = response.json()


    return data.get(
        "sent",
        False
    )
