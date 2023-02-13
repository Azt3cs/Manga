from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse
from .serializers import *
from .models import * 

def mangas(request,mangaid):
    return HttpResponse(f'Манга {mangaid}')

class MangaAPIView(generics.ListAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaSelializer