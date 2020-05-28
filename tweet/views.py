from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Tweet
from account.models import Account
from .forms import TweetForm


# Create your views here.


def tweet(request, pk):
    html = "twitterclone/tweetdetail.html"
    tweet = Tweet.objects.get(pk=pk)
    return render(request, html, {'tweet': tweet})


def addtweet(request):
    html = "twitterclone/newtweet.html"
    tweets = Tweet.objects.all().order_by('-id')
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Tweet.objects.create(
                tweet=data['tweet'],
                created_by=request.user,
            )
            messages.success(request, f'Your have  created new tweet.')
            return HttpResponseRedirect(reverse("homepage"))
    else:
        form = TweetForm()

    return render(request, html, {'form': form, 'tweets': tweets})
