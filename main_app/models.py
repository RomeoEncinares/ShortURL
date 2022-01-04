from django import shortcuts
from django.db import models

# Create your models here.

class Link(models.Model):
    url = models.CharField(max_length=1000)
    shortUrl = models.CharField(max_length=20)

    def __str__(self):
        return self.shortUrl