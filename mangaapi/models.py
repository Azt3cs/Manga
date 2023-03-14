from django.db import models


class Tovar(models.Model):
    title = models.CharField(max_length=30, blank=False)
    year = models.CharField(max_length=4, blank=False)
    description = models.TextField(blank=False)
    author = models.CharField(max_length=20, blank=False)
    genre = models.CharField(max_length=10, blank=False)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/')
    price = models.CharField(max_length=6, blank=False)
    stock = models.BooleanField()
    date = models.DateTimeField()
    titleManga = models.CharField(max_length=30, blank=False)
    type = models.CharField(blank=False, max_length=50)

    def __str__(self):
        return self.title


class Korzina(models.Model):
    tovarname = models.CharField(max_length=30)
    user = models.CharField(max_length=30)
    price = models.IntegerField()

    def __str__(self):
        return self.user
class Feedback(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    message = models.TextField()