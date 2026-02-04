import requests
from itertools import cycle
from django.conf import settings

keys = cycle(settings.YOUTUBE_API_KEYS)

def fetch_latest_videos(published_after):
    for _ in range(len(settings.YOUTUBE_API_KEYS)):
        key = next(keys)
        res = requests.get(
            "https://www.googleapis.com/youtube/v3/search",
            params={
                "key": key,
                "part": "snippet",
                "q": settings.YOUTUBE_SEARCH_QUERY,
                "type": "video",
                "order": "date",
                "publishedAfter": published_after,
                "maxResults": 25,
            },
        )
        if res.status_code == 200:
            return res.json()
    raise Exception("YouTube API quota exhausted")
