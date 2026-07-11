import re
import html


def get_media(url):

    media = []


    try:

        import requests


        response = requests.get(
            url,
            headers={
                "User-Agent":
                "Mozilla/5.0"
            },
            timeout=20
        )


        if response.status_code != 200:
            return []


        content = html.unescape(
            response.text
        )


        # اول ویدیوهای MP4

        videos = re.findall(
            r'https://video\.twimg\.com/[^"\s]+?\.mp4[^"\s]*',
            content
        )


        for video in videos:

            if video not in media:

                media.append(video)



        # بعد عکس‌ها

        images = re.findall(
            r'https://pbs\.twimg\.com/media/[^"\s]+',
            content
        )


        for image in images:

            image = image.split("?")[0]


            if image not in media:

                media.append(image)



        return media


    except Exception as e:

        print(
            "Media Error:",
            e
        )

        return []
