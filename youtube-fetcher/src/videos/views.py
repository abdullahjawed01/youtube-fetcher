from rest_framework.generics import ListAPIView
from django.contrib.postgres.search import SearchVector
from .models import Video
from .serializers import VideoSerializer

class VideoListView(ListAPIView):
    serializer_class = VideoSerializer
    queryset = Video.objects.order_by("-published_at")

class VideoSearchView(ListAPIView):
    serializer_class = VideoSerializer

    def get_queryset(self):
        q = self.request.query_params.get("q", "")
        return Video.objects.annotate(
            search=SearchVector("title", "description")
        ).filter(search=q).order_by("-published_at")
