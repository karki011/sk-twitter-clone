
from django.urls import path
from .views import tweetfeed


urlpatterns = [
    path("feed/", tweetfeed, name="feed")
]
