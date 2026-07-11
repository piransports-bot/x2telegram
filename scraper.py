import snscrape.modules.twitter as sntwitter


accounts = [
    "McLarenF1",
    "F1",
    "redbullracing"
]


for account in accounts:

    print("\nChecking:", account)


    scraper = sntwitter.TwitterUserScraper(
        account
    )


    for tweet in scraper.get_items():

        print("----------------")

        print(tweet.date)

        print(tweet.user.username)

        print(tweet.content)

        print(tweet.url)


        break
