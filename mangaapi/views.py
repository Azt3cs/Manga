from django.shortcuts import render
from rest_framework import generics, mixins
from django.http import HttpResponse

from .models import *
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.viewsets import GenericViewSet
from django.contrib.auth.views import LoginView

def index_page(request):
    manga = JapanManga.objects.all()
    manva = ChinaManva.objects.all()
    ranobe = JapanRanobe.objects.all()
    return render(request, 'mangaapi/index.html',{"manga":manga, "manva":manva, "ranobe":ranobe})

def manga_page(request):
    manga = JapanManga.objects.all()
    return render(request, 'mangaapi/manga.html', {'manga':manga})

def manva_page(request):
    manva = ChinaManva.objects.all()
    return render(request, 'mangaapi/manhva.html', {'manva':manva})

def ranobe_page(request):
    ranobe = JapanRanobe.objects.all()
    return render(request, 'mangaapi/ranobe.html', {'ranobe':ranobe})



# class MangaViewSet(mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.ListModelMixin,
#                    GenericViewSet):
#     queryset = Manga.objects.all()
#     serializer_class = MangaSelializer


# class ManvaViewSet(mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.ListModelMixin,
#                    GenericViewSet):
#     queryset = manva.objects.all()
#     serializer_class = ManvaSelializer


# class RanobeViewSet(mixins.CreateModelMixin,
#                     mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.ListModelMixin,
#                     GenericViewSet):
#     queryset = ranobe.objects.all()
#     serializer_class = RanobeSerializer

# class MangaAPIView(generics.ListAPIView):
#     queryset = Manga.objects.all()
#     serializer_class = MangaSelializer

# class ManvaAPIView(generics.ListAPIView):
#     queryset = manva.objects.all()
#     serializer_class = ManvaSelializer
#
# class RanobeAPIView(generics.ListAPIView):
#     queryset = ranobe.objects.all()
#     serializer_class = RanobeSerializer
