import os
import base64
from django.conf import settings
from django.db.models import Max, Count
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from users.models import User
from artistcategories.models import Artistcategories
from users.serializers import UserSerializer, UserLoginSerializer, CarouselSerializer
from artistcategories.serializers import ArtistcategoriesSerializer

# API for Users
class UserAPI(ModelViewSet):
          queryset = User.objects.all()
          serializer_class = UserSerializer

          def list(self, request, *args, **kwargs):
                    try:
                              user = User.objects.all()
                              serializer = self.get_serializer(user, many=True, context={'include_array_fields': True})
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'All user records',
                                        'all_users': serializer.data,
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_msg = 'An error occurred : {}'.format(str(e))
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                                        'message': error_msg,
                              }
                              return Response(error_response)

          def retrieve(self, request, *args, **kwargs):
                    try:
                              instance = self.get_object()
                              serializer = self.get_serializer(instance, context={'include_array_fields': True})
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'User by ID',
                                        'user_details': serializer.data,
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_msg = 'Failed to fetch details: {}'.format(str(e))
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_404_NOT_FOUND,
                                        'message': error_msg,
                              }
                              return Response(error_response)

          def create(self, request, *args, **kwargs):
                    try:
                              serializer = self.get_serializer(data=request.data, context={'include_array_fields': True})
                              serializer.is_valid(raise_exception=True)
                              serializer.save()
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_201_CREATED,
                                        'message': 'User created successfully',
                                        'new_user': serializer.data,
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_msg = 'Failed to add: {}'.format(str(e))
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_400_BAD_REQUEST,
                                        'message': error_msg,
                              }
                              return Response(error_response)

          def update(self, request, *args, **kwargs):
                    try:
                              instance = self.get_object()
                              serializer = self.get_serializer(instance, data=request.data, context={'include_array_fields': True})
                              serializer.is_valid(raise_exception=True)
                              serializer.save()
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'User updated successfully',
                                        'updated_user': serializer.data,
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_msg = 'Failed to update: {}'.format(str(e))
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_400_BAD_REQUEST,
                                        'message': error_msg,
                              }
                              return Response(error_response)

          def partial_update(self, request, *args, **kwargs):
                    try:
                              instance = self.get_object()
                              serializer = self.get_serializer(instance, data=request.data, partial=True, context={'include_array_fields': True})
                              serializer.is_valid(raise_exception=True)
                              serializer.save()
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'User partially updated successfully',
                                        'updated_user': serializer.data,
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_msg = 'Failed to partially update: {}'.format(str(e))
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_400_BAD_REQUEST,
                                        'message': error_msg,
                              }
                              return Response(error_response)

          def destroy(self, request, *args, **kwargs):
                    try:
                              instance = self.get_object()
                              instance.delete()
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'User deleted successfully',
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_msg = 'Failed to delete: {}'.format(str(e))
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_400_BAD_REQUEST,
                                        'message': error_msg,
                              }
                              return Response(error_response)

          def artistsList(self, request, *args, **kwargs):
                    try:
                              artists = User.objects.filter(utypeartist=1)
                              serializer = self.get_serializer(artists, many=True, context={'include_array_fields': True})
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'All artist records',
                                        'artists_list': serializer.data,
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_msg = 'An error occurred: {}'.format(str(e))
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                                        'message': error_msg,
                              }
                              return Response(error_response)

          def organizersList(self, request, *args, **kwargs):
                    try:
                              organizers = User.objects.filter(utypeorganizer=1)
                              serializer = self.get_serializer(organizers, many=True, context={'include_array_fields': True})
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'All organizer records',
                                        'organizers_list': serializer.data,
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_msg = 'An error occurred: {}'.format(str(e))
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                                        'message': error_msg,
                              }
                              return Response(error_response)

          def usersList(self, request, *args, **kwargs):
                    try:
                              users = User.objects.filter(utypeuser=1)
                              serializer = self.get_serializer(users, many=True, context={'include_array_fields': True})
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'All user records',
                                        'users_list': serializer.data,
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_msg = 'An error occurred: {}'.format(str(e))
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                                        'message': error_msg,
                              }
                              return Response(error_response)

class UserLoginAPI(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            uname = serializer.validated_data.get('uname')
            upassword = serializer.validated_data.get('upassword')

            try:
                user = User.objects.get(uname=uname)

                if user.upassword == upassword:
                    user_type = None

                    if user.utypeartist == serializer.validated_data.get('utypeartist', False):
                        if user.utypeorganizer == serializer.validated_data.get('utypeorganizer', False):
                            if user.utypeuser == serializer.validated_data.get('utypeuser', False):
                                if user.utypeartist:
                                    user_type = 'artist'
                                elif user.utypeorganizer:
                                    user_type = 'organizer'
                                elif user.utypeuser:
                                    user_type = 'user'

                                return Response({'message': 'Valid User', 'user_type': user_type}, status=status.HTTP_200_OK)
                            else:
                                return Response({'message': 'Invalid usertype'}, status=status.HTTP_401_UNAUTHORIZED)
                        else:
                            return Response({'message': 'Invalid organizertype'}, status=status.HTTP_401_UNAUTHORIZED)
                    else:
                        return Response({'message': 'Invalid artisttype'}, status=status.HTTP_401_UNAUTHORIZED)
                else:
                    return Response({'message': 'Invalid Password'}, status=status.HTTP_401_UNAUTHORIZED)
            except User.DoesNotExist:
                return Response({'message': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArtistByCategoryAPI(generics.ListAPIView):
          serializer_class = UserSerializer

          def list(self, request, cname, scname, *args, **kwargs):
                    category_obj = Artistcategories.objects.filter(cname=cname).first()
                    subcategory_obj = Artistcategories.objects.filter(scname=scname).first()

                    if category_obj or subcategory_obj:
                              artists = User.objects.filter(utypeartist=1, acategory=cname, asubcategory=scname)
                              serializer = self.get_serializer(artists, many=True)
                              data = serializer.data
                              response_data = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'Artists fetched successfully',
                                        'artistbycategory': data
                              }
                              return Response(response_data)

                    response_data = {
                              'status': 'error',
                              'code': status.HTTP_400_BAD_REQUEST,
                              'message': 'Invalid category or subcategory provided.',
                              'data': []
                    }
                    return Response(response_data)

class UserCountAPI(generics.ListAPIView):
          serializer_class = UserSerializer

          def list(self, request, *args, **kwargs):
                    try:
                              total_users = User.objects.count()
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'Total count of users',
                                        'count': total_users,
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_msg = 'An error occured: {}'.format(str(e))
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_400_BAD_REQUEST,
                                        'message': error_msg,
                              }
                              return Response(error_response)

class CarouselAPI(APIView):
    serializer_class = CarouselSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            # Access each image field separately
            image1 = serializer.validated_data.get('image1')
            image2 = serializer.validated_data.get('image2')
            image3 = serializer.validated_data.get('image3')
            image4 = serializer.validated_data.get('image4')
            image5 = serializer.validated_data.get('image5')

            # Specify the folder path for storing image files
            folder_name = 'carousel_images'
            folder_path = os.path.join(settings.MEDIA_ROOT, folder_name)

            # Create the folder if it doesn't exist
            os.makedirs(folder_path, exist_ok=True)

            # Loop through each image and save it as an image file
            saved_file_paths = []
            for index, image_data in enumerate([image1, image2, image3, image4, image5]):
                image_name = f'image{index}.png'  # Change the extension based on your requirements
                save_path = os.path.join(folder_path, image_name)

                try:
                    # Write the base64 code to the file
                    with open(save_path, 'wb') as image_file:
                        image_file.write(base64.b64decode(image_data))
                except Exception as e:
                    # Handle file writing errors
                    error_message = f"Error saving image {index}: {str(e)}"
                    return Response({"error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

                saved_file_paths.append(save_path)

            response_data = {
                'status': 'success',
                'code': status.HTTP_201_CREATED,
                'message': 'Base64 codes converted to images successfully',
                'saved_file_paths': saved_file_paths
            }
            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

