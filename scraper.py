import requests
from bs4 import BeautifulSoup


accounts = [
    "McLarenF1",
    "F1",
    "redbullracing"
]


headers = {
    "User-Agent":
    "Mozilla/5.0"
}


for account in accounts:

    print("\nChecking:", account)


    url = f"https://x.com/{account}"


    response = requests.get(
        url,
        headers=headers,
        timeout=20
    )


    print(
        "Status:",
        response.status_code
    )


    if response.status_code == 200:

        soup = BeautifulSoup(
            response.text,
            "lxml"
        )


        text = soup.get_text(
            " ",
            strip=True
        )


        print(
            text[:500]
        )


    else:

        print(
            "Failed"
        )
