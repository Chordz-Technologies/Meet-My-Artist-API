from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
          class Meta:
                    model = User
                    fields = '__all__'

          def to_representation(self, instance):
                    representation = super().to_representation(instance)

                    # Fields for which you want array-type response
                    array_fields = [
                              'alikes',
                              'aphotos',
                              'awishlist',
                              'owishlist',
                              'olikes',
                              'ophotos',
                              'ulikes',
                              'uwishlist',
                              # Add more fields as needed
                    ]

                    for field in array_fields:
                              if field in representation and representation[field] is not None:
                                        if representation[field].strip() == '':
                                                  representation[field] = []
                                        else:
                                                  representation[field] = representation[field].split(',')

                    return representation

class UserLoginSerializer(serializers.Serializer):
          uemail = serializers.CharField(required=True)
          upassword = serializers.CharField(required=True)
          utypeartist = serializers.IntegerField(required=True)
          utypeorganizer = serializers.IntegerField(required=True)
          utypeuser = serializers.IntegerField(required=True)

class CarouselSerializer(serializers.Serializer):
          image1 = serializers.CharField(required=False)
          image2 = serializers.CharField(required=False)
          image3 = serializers.CharField(required=False)
          image4 = serializers.CharField(required=False)
          image5 = serializers.CharField(required=False)

          def validate(self, attrs):
                    # Remove empty fields from the validated data
                    validated_data = {key: value for key, value in attrs.items() if value.strip()}
                    return validated_data
