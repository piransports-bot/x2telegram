import requests
import json
from bs4 import BeautifulSoup
from tweet_parser import extract_tweet


accounts = [
    "McLarenF1",
    "F1",
    "redbullracing"
]


headers = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "Chrome/120 Safari/537.36"
    )
}


def get_account_page(username):

    url = f"https://x.com/{username}"

    try:

        response = requests.get(
            url,
            headers=headers,
            timeout=20
        )

        print(
            "\nChecking:",
            username
        )

        print(
            "Status:",
            response.status_code
        )


        if response.status_code == 200:

            return response.text


        return None


    except Exception as e:

        print(
            "Request error:",
            e
        )

        return None



def main():


    all_tweets = []


    for account in accounts:


        html = get_account_page(
            account
        )


        if not html:

            continue


        tweets = extract_tweet(
            html
        )


        for tweet in tweets:

            tweet["user"] = account

            all_tweets.append(
                tweet
            )


    print(
        "\n========== RESULT =========="
    )


    print(
        json.dumps(
            all_tweets,
            indent=2,
            ensure_ascii=False
        )
    )



if __name__ == "__main__":

    main()
