
from django.contrib import admin
from django.urls import path
from mangaapi.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('manga/<int:mangaid>', mangas ),
    path('api/v1/manga/', MangaAPIView.as_view() )

]
