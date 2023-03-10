from django.shortcuts import render
from rest_framework import generics, mixins
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.viewsets import GenericViewSet
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator

def index_page(request):
    manga = JapanManga.objects.all()
    manva = ChinaManva.objects.all()
    ranobe = JapanRanobe.objects.all()
    return render(request, 'mangaapi/index.html',{"manga": manga, "manva":manva,"ranobe":ranobe})

def manga_page(request):
    manga = JapanManga.objects.all()
    return render(request, 'mangaapi/manga.html',{"manga":manga})
def manga_id(request, manga_id):
    manga = JapanManga.objects.filter(id=manga_id)
    return render(request, 'mangaapi/about.html',{'manga':manga})

def manva_id(request, manva_id):
    manva = ChinaManva.objects.filter(id=manva_id)
    return render(request, 'mangaapi/aboutManhva.html',{'manva':manva})

def ranobe_id(request, ranobe_id):
    ranobe = JapanRanobe.objects.filter(id=ranobe_id)
    return render(request, 'mangaapi/aboutRanobe.html',{'ranobe':ranobe})

def manva_page(request):
    manva = ChinaManva.objects.all()
    return render(request, 'mangaapi/manhva.html', {"manva":manva})

def ranobe_page(request):
    ranobe = JapanRanobe.objects.all()
    return render(request, 'mangaapi/ranobe.html', {"ranobe":ranobe})