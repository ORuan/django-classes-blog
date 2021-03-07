from django.db import models as m
from django.utils import timezone
from django.contrib.auth.models import User


class Post(m.Model):
    title = m.CharField(max_length=100)
    content = m.TextField()
    date_posted = m.DateTimeField(default=timezone.now)
    author = m.ForeignKey(User, on_delete=m.CASCADE)
    
    def __str__(self):
        return self.title