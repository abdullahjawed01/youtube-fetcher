from django.urls import path
from .views import VideoListView, VideoSearchView

urlpatterns = [
    path("videos/", VideoListView.as_view()),
    path("videos/search/", VideoSearchView.as_view()),
]
