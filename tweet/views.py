from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Tweet
from account.models import Account


# Create your views here.

def tweetfeed(request):
    html = 'twitterclone/feed.html'
    tweets = Tweet.objects.all().order_by('-id')
    print(tweets)
    return render(request, html, {'tweets': tweets})
