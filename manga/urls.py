from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from manga import settings
from mangaapi.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name='main'),
    path('manga/', manga_page, name='manga'),
    path('manga/<int:manga_id>/', manga_id, name='manga_id'),
    path('manva/<int:manva_id>/', manva_id, name='manva_id'),
    path('ranobe/<int:ranobe_id>/', ranobe_id, name='ranobe_id'),
    path('manva/', manva_page, name='manva'),
    path('ranobe/', ranobe_page, name='ranobe'),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
