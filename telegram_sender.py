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



def send_album(photos, caption):


    media = []


    for index, photo in enumerate(photos):

        item = {

            "type": "photo",

            "media": photo

        }


        # کپشن فقط روی عکس اول

        if index == 0:

            item["caption"] = caption

            item["parse_mode"] = "HTML"



        media.append(item)



    requests.post(

        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMediaGroup",

        json={

            "chat_id": CHAT_ID,

            "media": media

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



    videos = []

    photos = []



    for item in media:


        if ".mp4" in item:

            videos.append(
                item
            )


        elif "pbs.twimg.com" in item:

            # حذف تکراری های jpg

            clean = item.split("?")[0]


            if clean not in photos:

                photos.append(
                    clean
                )



    # اگر ویدیو وجود داشت

    if videos:


        send_video(

            videos[0],

            caption

        )

        return



    # اگر چند عکس بود

    if len(photos) > 1:


        send_album(

            photos,

            caption

        )

        return



    # یک عکس

    if len(photos) == 1:


        send_photo(

            photos[0],

            caption

        )

        return



    send_message(
        caption
    )
