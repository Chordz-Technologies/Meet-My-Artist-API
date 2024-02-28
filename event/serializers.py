from rest_framework import serializers
from event.models import Events

class EventSerializer(serializers.ModelSerializer):
          class Meta:
                    model = Events
                    fields = '__all__'

class EventPosterSerializer(serializers.Serializer):
          eventid = serializers.IntegerField()
          poster = serializers.CharField()
