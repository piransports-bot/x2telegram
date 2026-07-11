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



        # گرفتن ویدیوهای MP4

        videos = re.findall(

            r'https://video\.twimg\.com/[^"\s]+?\.mp4[^"\s]*',

            content

        )



        video_list = []



        for video in videos:


            if video not in video_list:

                video_list.append(
                    video
                )



        # مرتب سازی کیفیت ویدیو


        def video_quality(link):


            match = re.search(

                r'/(\d+)x(\d+)/',

                link

            )


            if match:


                width = int(
                    match.group(1)
                )


                height = int(
                    match.group(2)
                )


                return width * height



            return 0



        video_list.sort(

            key=video_quality,

            reverse=True

        )



        for video in video_list:


            if video not in media:

                media.append(
                    video
                )



        # گرفتن عکس‌ها

        images = re.findall(

            r'https://pbs\.twimg\.com/media/[^"\s]+',

            content

        )



        for image in images:


            image = image.split("?")[0]



            if image not in media:

                media.append(
                    image
                )



        return media



    except Exception as e:


        print(

            "Media Error:",

            e

        )


        return []
