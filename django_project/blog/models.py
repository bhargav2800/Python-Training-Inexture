from email import contentmanager
from django.shortcuts import render, redirect
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # It will show post by title --- we have use dunder/magic method
    def __str__(self):
        return self.title

    #Used to reverse to the created post url
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk' : self.pk})
    