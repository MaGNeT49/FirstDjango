from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)


class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Create your models here.
