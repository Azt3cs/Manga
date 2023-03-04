import imghdr
from django.db import models


class JapanManga(models.Model):
    title = models.CharField(max_length=30, blank=False)
    year = models.CharField(max_length=4, blank=False)
    description = models.TextField(blank=False)
    author = models.CharField(max_length=20, blank=False)
    genre = models.CharField(max_length=10, blank=False, primary_key=True)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/')
    price = models.CharField(max_length=6, blank=False)
    stock = models.BooleanField()
    date = models.DateTimeField()
    titleManga = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.title


class ChinaManva(models.Model):
    title = models.CharField(max_length=30, blank=False)
    year = models.CharField(max_length=4, blank=False)
    description = models.TextField()
    author = models.CharField(max_length=20, blank=False)
    genre = models.CharField(max_length=10, blank=False)
    photos = models.ImageField(upload_to='photoManva/%Y/%m/%d/')
    price = models.CharField(max_length=6, blank=False)
    stock = models.BooleanField()
    date = models.DateTimeField()


class JapanRanobe(models.Model):
    title = models.CharField(max_length=30, blank=False)
    year = models.CharField(max_length=4, blank=False)
    description = models.TextField()
    author = models.CharField(max_length=20, blank=False)
    genre = models.CharField(max_length=10, blank=False)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/')
    price = models.CharField(max_length=6, blank=False)
    stock = models.BooleanField()
    date = models.DateTimeField()
