import json
import requests

from tweet_parser import extract_tweet
from tweet_details import get_tweet_details


accounts = [
    "McLarenF1",
    "F1",
    "redbullracing"
]


headers = {
    "User-Agent":
    "Mozilla/5.0"
}



def get_account_page(username):

    url = f"https://x.com/{username}"


    response = requests.get(
        url,
        headers=headers,
        timeout=20
    )


    if response.status_code == 200:

        return response.text


    return None



def main():


    results = []


    for account in accounts:


        print(
            "\nChecking:",
            account
        )


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


            if details:

                details["user"] = account

                results.append(
                    details
                )



    print(
        json.dumps(
            results,
            indent=2,
            ensure_ascii=False
        )
    )



if __name__ == "__main__":
    main()
