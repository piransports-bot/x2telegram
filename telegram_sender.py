import os
import requests


BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")



def send_message(text):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"


    requests.post(
        url,
        json={
            "chat_id": CHAT_ID,
            "text": text,
            "parse_mode": "HTML"
        }
    )



def send_photo(photo, caption):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"


    requests.post(
        url,
        json={
            "chat_id": CHAT_ID,
            "photo": photo,
            "caption": caption,
            "parse_mode": "HTML"
        }
    )



def send_video(video, caption):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendVideo"


    requests.post(
        url,
        json={
            "chat_id": CHAT_ID,
            "video": video,
            "caption": caption,
            "parse_mode": "HTML"
        }
    )



def send_tweet(tweet):


    caption = (
        f"🏎 <b>{tweet['user']}</b>\n\n"
        f"{tweet['text']}\n\n"
        f"🔗 {tweet['url']}"
    )


    media = tweet.get(
        "media",
        []
    )


    if not media:

        send_message(
            caption
        )

        return



    first = media[0]


    # تشخیص واقعی ویدیو

    if (
        "video.twimg.com" in first
        or
        ".mp4" in first
    ):

        send_video(
            first,
            caption
        )


    else:

        send_photo(
            first,
            caption
        )
