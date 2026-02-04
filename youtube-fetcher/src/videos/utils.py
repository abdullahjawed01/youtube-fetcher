import os
import itertools

YOUTUBE_API_KEYS = list(
    filter(
        None,
        [
            os.getenv("YOUTUBE_API_KEY_1"),
            os.getenv("YOUTUBE_API_KEY_2"),
            os.getenv("YOUTUBE_API_KEY_3"),
        ],
    )
)

_key_cycle = itertools.cycle(YOUTUBE_API_KEYS)

def get_api_key():
    if not YOUTUBE_API_KEYS:
        raise RuntimeError("No YouTube API keys configured")
    return next(_key_cycle)
