from django.db import models
from django.contrib.auth.models import User


class tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    photo = models.ImageField(upload_to="tweet_images/", blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return f"{self.user} added {self.text} at {self.date_created}"


# Create your models here.
