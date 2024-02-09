from rest_framework import serializers
from .models import Artistcategories

class ArtistcategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artistcategories
        fields = '__all__'