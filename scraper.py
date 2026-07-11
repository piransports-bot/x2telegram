import json
import requests

from tweet_parser import extract_tweet
from tweet_details import get_tweet_details
from tweet_media import get_media
from telegram_sender import send_tweet
from tweet_cache import check_tweet


headers = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "Chrome/120 Safari/537.36"
    )
}


def load_accounts():

    with open(
        "accounts.json",
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)



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
            "Page error:",
            e
        )

        return None



def main():

    results = []


    accounts = load_accounts()


    print(
        "Accounts loaded:",
        len(accounts)
    )


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



            tweet_id = (
                details["url"]
                .split("/")
                [-1]
            )



            print(
                "\nChecking tweet:",
                tweet_id
            )



            if check_tweet(tweet_id):

                print(
                    "Already sent:",
                    tweet_id
                )

                continue



            print(
                "\nNew tweet found:"
            )


            print(
                json.dumps(
                    details,
                    indent=2,
                    ensure_ascii=False
                )
            )



            send_tweet(
                details
            )


            results.append(
                details
            )



    print(
        "\n========== DONE =========="
    )


    print(
        "Sent:",
        len(results)
    )



if __name__ == "__main__":

    main()
