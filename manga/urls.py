from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from manga import settings
from mangaapi.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name='main'),
    path('catalog/manga', manga_page, name='manga'),
    path('catalog/manga/korzina_page', korzina_page, name='korzina_page'),
    path('catalog/manhva', manva_page, name='manva'),
    path('catalog/ranobe', ranobe_page, name='ranobe'),
    path('manga/<int:tovar_id>/', tovar_id, name='tovar_id'),
    path('accounts/', include('allauth.urls')),
    path('profile/', profile_page, name='profile'),
    path('feedback/',feedback_page,name='feed'),
    path('feedback/feedback', feedback, name='back')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
