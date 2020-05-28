from django.db import models
from tweet.models import Tweet
from account.models import Account


# Create your models here.
class Notification(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    viewed = models.BooleanField(default=False)
    notify = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.tweet
