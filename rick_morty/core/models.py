from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):

    author = models.TextField() #models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    episode = models.IntegerField()

    class Meta:
        ordering = ['created_on']