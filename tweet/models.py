from django.db import models
from django.utils import timezone
from account.models import Account


class Tweet(models.Model):
    tweet = models.CharField(max_length=120)
    created_by = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='tweets')
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.tweet
