import requests
from celery import shared_task
from django.utils.dateparse import parse_datetime
from django.utils.timezone import make_aware
from .models import Video
from .utils import get_api_key

YOUTUBE_SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"

@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=5)
def fetch_latest_videos(self):
    params = {
        "part": "snippet",
        "q": "tea",
        "type": "video",
        "order": "date",
        "maxResults": 25,
        "key": get_api_key(),
    }

    response = requests.get(YOUTUBE_SEARCH_URL, params=params)
    response.raise_for_status()

    for item in response.json()["items"]:
        snippet = item["snippet"]

        published_at = parse_datetime(snippet["publishedAt"])
        if published_at and not published_at.tzinfo:
            published_at = make_aware(published_at)

        Video.objects.update_or_create(
            video_id=item["id"]["videoId"],
            defaults={
                "title": snippet["title"],
                "description": snippet["description"],
                "published_at": published_at,
                "thumbnail_url": snippet["thumbnails"]["high"]["url"],
                "channel_title": snippet["channelTitle"],
            },
        )
