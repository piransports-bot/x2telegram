import os
import requests


BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")



def send_message(text):

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={
            "chat_id": CHAT_ID,
            "text": text,
            "parse_mode": "HTML"
        }
    )



def send_photo(photo, caption):

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto",
        json={
            "chat_id": CHAT_ID,
            "photo": photo,
            "caption": caption,
            "parse_mode": "HTML"
        }
    )



def send_video(video, caption):

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendVideo",
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



    # پیدا کردن MP4 واقعی

    video = None

    photo = None


    for item in media:

        if ".mp4" in item:

            video = item
            break


        if "pbs.twimg.com" in item:

            photo = item



    if video:

        send_video(
            video,
            caption
        )


    elif photo:

        send_photo(
            photo,
            caption
        )


    else:

        send_message(
            caption
        )
