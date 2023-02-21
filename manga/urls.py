from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from manga import settings
from mangaapi.views import *

router = routers.DefaultRouter()
router.register(r'manga', MangaViewSet)
router.register(r'ranobe',RanobeViewSet)
router.register(r'manhva',ManvaViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('manga/<int:mangaid>', mangas),
    path('api/v1/', include(router.urls)),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
