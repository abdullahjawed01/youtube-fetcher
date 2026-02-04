from django.db import models

class Video(models.Model):
    video_id = models.CharField(max_length=100, unique=True)
    title = models.TextField(db_index=True)
    description = models.TextField()
    published_at = models.DateTimeField(db_index=True)
    thumbnail_url = models.URLField()
    channel_title = models.CharField(max_length=255)

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.title
