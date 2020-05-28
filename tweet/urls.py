
from django.urls import path
from .views import tweet, addtweet


urlpatterns = [
    path('tweet/<int:pk>', tweet, name='tweet'),
    path("", addtweet, name="homepage"),
]
