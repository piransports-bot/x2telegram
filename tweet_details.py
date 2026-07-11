import requests
from bs4 import BeautifulSoup


headers = {
    "User-Agent":
    "Mozilla/5.0"
}


def get_tweet_details(url):

    try:

        response = requests.get(
            url,
            headers=headers,
            timeout=20
        )


        if response.status_code != 200:
            return None


        soup = BeautifulSoup(
            response.text,
            "lxml"
        )


        text = ""


        meta = soup.find(
            "meta",
            attrs={
                "property":
                "og:description"
            }
        )


        if meta:
            text = meta.get(
                "content",
                ""
            )


        return {

            "url": url,

            "text": text

        }


    except Exception as e:

        print(
            "Detail error:",
            e
        )

        return None
