from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from .models import Tweet
from account.models import Account
from .forms import TweetForm


# Create your views here.

@login_required()
def tweet(request, pk):
    html = "twitterclone/tweetdetail.html"
    tweet = Tweet.objects.get(pk=pk)
    return render(request, html, {'tweet': tweet})


class UserTweetListView(TemplateView):
    model = Tweet
    template_name = 'twitterclone/user_tweet.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(Account, username=self.kwargs.get('username'))
        context['tweets'] = Tweet.objects.filter(created_by=user).order_by('-date_created')
        context['viewed_user'] = Account.objects.get(username=user)
        return context


@login_required()
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


@login_required()
def follow_user(request, username):
    if request.user.is_authenticated:
        my_user = Account.objects.get(username=request.user.username)
        viewed_user = Account.objects.get(username=username)
        my_user.following.add(viewed_user)
        my_user.save()
    return redirect("/user/" + username)


@login_required()
def unfollow_user(request, username):
    if request.user.is_authenticated:
        my_user = Account.objects.get(username=request.user.username)
        viewed_user = Account.objects.get(username=username)
        my_user.following.remove(viewed_user)
        my_user.save()
    return redirect("/user/" + username)
