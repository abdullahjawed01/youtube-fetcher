from .base import *

DEBUG = True

# ---------- STATIC FILES ----------
STATIC_URL = "/static/"

# ---------- CELERY ----------
CELERY_BROKER_URL = "redis://redis:6379/0"
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"


