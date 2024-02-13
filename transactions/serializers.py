from rest_framework import serializers
from transactions.models import Atransaction, Otransaction, Utransaction

class AtSerializer(serializers.ModelSerializer):
          class Meta:
                    model = Atransaction
                    fields = '__all__'

class OtSerializer(serializers.ModelSerializer):
          class Meta:
                    model = Otransaction
                    fields = '__all__'

class UtSerializer(serializers.ModelSerializer):
          class Meta:
                    model = Utransaction
                    fields = '__all__'