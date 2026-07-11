import re
import json


def extract_tweet(html):

    tweets = []


    urls = re.findall(
        r'https://x\.com/[^"]+/status/\d+',
        html
    )


    for url in urls:

        tweets.append({

            "url": url

        })


    return tweets



if __name__ == "__main__":

    print(
        "Parser Ready"
    )
