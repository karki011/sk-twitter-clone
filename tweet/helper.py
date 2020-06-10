import re

from notification.models import Notification
from account.models import Account


def send_notifications(tweet):
    if "@" in tweet.tweet:
        users = find_mentioned_users(tweet.tweet)
        for user in users:
            if user in [x.username for x in Account.objects.all()]:
                Notification.objects.create(tweet=tweet, notify=Account.objects.get(username=user),viewed=False)


def find_mentioned_users(tweet):
    mentioned_users = re.findall(r"@(\w+)\b", tweet)
    return mentioned_users
