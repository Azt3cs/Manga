from rest_framework import serializers
from .models import *


class MangaSelializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = '__all__'


class ManvaSelializer(serializers.ModelSerializer):
    class Meta:
        model = manva
        fields = '__all__'


class RanobeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ranobe
        fields = '__all__'
