from rest_framework import serializers
from .models import *
class MangaSelializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = '__all__'