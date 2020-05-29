from django.urls import path
from .views import tweet, addtweet, UserTweetListView, follow_user, unfollow_user

urlpatterns = [
    path('tweet/<int:pk>', tweet, name='tweet'),
    path("", addtweet, name="homepage"),
    path('user/<str:username>/', UserTweetListView.as_view(), name="usertweet"),
    path('user/<str:username>/follow', follow_user, name="follow_user"),
    path('user/<str:username>/unfollow', unfollow_user, name="unfollow_user")

]
