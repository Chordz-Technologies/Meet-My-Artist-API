from rest_framework import serializers
from businesscategories.models import Businesscategories

class BusinessSerializer(serializers.ModelSerializer):
          class Meta:
                    model = Businesscategories
                    fields = '__all__'