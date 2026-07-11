import requests
import re


headers = {
    "User-Agent":
    "Mozilla/5.0"
}



def get_media(url):

    media = []


    try:

        response = requests.get(
            url,
            headers=headers,
            timeout=20
        )


        if response.status_code != 200:

            return media



        html = response.text



        # پیدا کردن عکس‌ها

        images = re.findall(
            r'https://pbs\.twimg\.com/media/[^"\?]+',
            html
        )


        for image in images:

            if image not in media:

                media.append(
                    image
                )



        # پیدا کردن ویدیو

        videos = re.findall(
            r'https://video\.twimg\.com/[^"\s]+',
            html
        )


        for video in videos:

            if video not in media:

                media.append(
                    video
                )


        return media



    except Exception as e:

        print(
            "Media error:",
            e
        )

        return media
