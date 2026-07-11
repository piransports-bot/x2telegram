import json
import requests

from tweet_parser import extract_tweet
from tweet_details import get_tweet_details
from tweet_media import get_media
from telegram_sender import send_tweet


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

        print("\nChecking:", username)
        print("Status:", response.status_code)


        if response.status_code == 200:

            return response.text


        return None


    except Exception as e:

        print(
            "Account page error:",
            e
        )

        return None



def main():

    results = []


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


            details = get_tweet_details(
                tweet["url"]
            )


            if not details:

                continue



            details["user"] = account



            details["media"] = get_media(
                details["url"]
            )



            results.append(
                details
            )


            print(
                "\nTweet Found:"
            )


            print(
                json.dumps(
                    details,
                    indent=2,
                    ensure_ascii=False
                )
            )



            # ارسال به تلگرام

            send_tweet(
                details
            )



    print(
        "\n========== TOTAL =========="
    )


    print(
        len(results),
        "tweets processed"
    )



if __name__ == "__main__":

    main()
