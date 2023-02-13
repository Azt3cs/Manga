import imghdr
from django.db import models



class Manga(models.Model):
 
    title = models.CharField(max_length=30,blank=False)
    year = models.CharField(max_length=4,blank=False)
    description = models.TextField()
    author = models.CharField(max_length=20,blank=False)
    genre =models.CharField(max_length=10,blank=False)

    def __str__(self):
        return self.title

class manva(models.Model):
 
    title = models.CharField(max_length=30,blank=False)
    year = models.CharField(max_length=4,blank=False)
    description = models.TextField()
    author = models.CharField(max_length=20,blank=False)
    genre =models.CharField(max_length=10,blank=False)

class ranobe(models.Model):
  
    title = models.CharField(max_length=30,blank=False)
    year = models.CharField(max_length=4,blank=False)
    description = models.TextField()
    author = models.CharField(max_length=20,blank=False)
    genre =models.CharField(max_length=10,blank=False)
