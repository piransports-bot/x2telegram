import re
import requests


headers = {
    "User-Agent": "Mozilla/5.0"
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


        # ویدیوهای واقعی X

        videos = re.findall(
            r'https://video\.twimg\.com/[^"\\]+\.mp4',
            html
        )


        for video in videos:

            video = video.replace("\\u0026","&")

            if video not in media:
                media.append(video)



        # عکس‌ها

        images = re.findall(
            r'https://pbs\.twimg\.com/media/[^"\\?]+',
            html
        )


        for image in images:

            if image not in media:
                media.append(image)



        return media



    except Exception as e:

        print(
            "Media Error:",
            e
        )

        return []
