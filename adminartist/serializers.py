from rest_framework import serializers
from adminartist.models import Adminartist

class AdminSerializer(serializers.ModelSerializer):
          class Meta:
                    model = Adminartist
                    fields = '__all__'

class AdminLoginSerializer(serializers.Serializer):
    aname = serializers.CharField(required=True)
    apassword = serializers.CharField(required=True)
