import re


def extract_tweet(html):

    tweets = []


    urls = re.findall(
        r'https://x\.com/[^"\s]+/status/\d+',
        html
    )


    # حذف تکراری‌ها با حفظ ترتیب

    seen = set()


    for url in urls:

        if url not in seen:

            seen.add(url)

            tweets.append({
                "url": url
            })


    # فقط 10 توییت آخر

    return tweets[:10]
