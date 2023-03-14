from django.shortcuts import render
from rest_framework import generics, mixins
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.viewsets import GenericViewSet
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator

def index_page(request):
    tovar = Tovar.objects.all()
    return render(request, 'mangaapi/index.html', {'tovar':tovar})

def manga_page(request):
    tovar = Tovar.objects.all()
    return render(request, 'mangaapi/manga.html', {'tovar':tovar})
def manva_page(request):
    tovar = Tovar.objects.all()
    return render(request, 'mangaapi/manhva.html', {'tovar':tovar})
def ranobe_page(request):
    tovar = Tovar.objects.all()
    return render(request, 'mangaapi/ranobe.html', {'tovar':tovar})
def tovar_id(request, tovar_id):
    tovar = Tovar.objects.filter(id=tovar_id)
    return render(request, 'mangaapi/about.html', {'tovar':tovar})


def profile_page(request):
    return render(request, 'mangaapi/profile.html')

def korzina_page(request):

    if request.method == 'POST':
        korzina = Korzina()
        korzina.name = request.POST.get("tovarname")
        korzina.price = request.POST.get("price")
        korzina.username = request.POST.get("name")
        korzina.save()
    return HttpResponseRedirect("/")


def feedback_page(request):
    feedback = Feedback.objects.all()
    return render(request, 'mangaapi/feedback.html',{'fb':feedback})

def feedback(request):
    if request.method == 'POST':
        feedback = Feedback()
        feedback.name = request.POST.get("name")
        feedback.email =request.POST.get("email")
        feedback.message =request.POST.get("message")
        feedback.save()
    return HttpResponseRedirect("/feedback")