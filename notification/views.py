from django.shortcuts import render, redirect
from tweet.models import Tweet
from account.models import Account
from .models import Notification


def notifications(request):
    if request.user.is_authenticated:
        html = 'twitterclone/notification.html'
        notifications = Notification.objects.filter(notify=request.user).filter(viewed=False)
        print('notes', notifications)
        new_tweets = Tweet.objects.filter(
            id__in=[x.tweet.id for x in notifications]).order_by(
            "-id")
        for notification in notifications:
            notification.viewed = True
            notification.save()
        accuser = Account.objects.get(id=request.user.id)
        return render(request, html, {
            'new_tweets': new_tweets,
            'notifications': notifications,
            'accuser': accuser})
    return redirect('/login/')
