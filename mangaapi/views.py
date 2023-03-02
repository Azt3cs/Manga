from django.shortcuts import render
from rest_framework import generics, mixins
from django.http import HttpResponse
from .serializers import *
from .models import *

from rest_framework.viewsets import GenericViewSet


def index_page(request):
    manga = Manga.objects.all()
    return render(request, 'mangaapi/index.html',{"manga":manga})


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
