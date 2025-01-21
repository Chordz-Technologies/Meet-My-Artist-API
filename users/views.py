import ast
import os
import base64
import operator
from functools import reduce
from PIL import Image
from io import BytesIO
from django.db import transaction
from django.core.exceptions import RequestDataTooBig
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse, HttpRequest
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.db.models import Max, Count, CharField, TextField, Q
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from users.models import User
from event.models import Events
from products.models import Products
from artistcategories.models import Artistcategories
from users.serializers import UserSerializer, UserLoginSerializer, CarouselSerializer, ProfilePhotoSerializer, \
          MultiplePhotosSerializer
from users.serializers import UserSerializer, UserLoginSerializer, CarouselSerializer
from event.serializers import EventSerializer
from products.serializers import ProductSerializer
from artistcategories.serializers import ArtistcategoriesSerializer
from businesscategories.models import Businesscategories

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

          def search(self, request, *args, **kwargs):
                    try:
                              search_term = request.query_params.get('search_term', '').lower()
                              if not search_term:
                                        return Response({"message": "Please provide a search term"},
                                                        status=status.HTTP_400_BAD_REQUEST)

                              # List of models you want to search
                              models_to_search = [Events, Products, User]

                              # Initialize dictionary to store search results for each model
                              search_results = {}

                              # Iterate through each model and perform the search
                              for model in models_to_search:
                                        queryset = self.filter_model_by_search_term(model, search_term)
                                        search_results[model.__name__] = queryset

                              # Check if any results are found
                              total_records = {model_name: queryset.count() for model_name, queryset in
                                               search_results.items()}
                              if any(total_records.values()):
                                        # Process and serialize the search results for each model
                                        serialized_results = {}
                                        for model_name, queryset in search_results.items():
                                                  serializer_class = self.get_serializer_class_for_model(
                                                            model_name)  # Pass model name
                                                  serializer = serializer_class(queryset, many=True)
                                                  # Separate users based on their type
                                                  if model_name == 'User':
                                                            users = serializer.data
                                                            user_types = {'artists': [], 'organizers': []}
                                                            for user in users:
                                                                      if user['utypeartist'] == 1:
                                                                                user_types['artists'].append(user)
                                                                      if user['utypeorganizer'] == 1:
                                                                                user_types['organizers'].append(user)
                                                            serialized_results[model_name] = user_types
                                                  else:
                                                            serialized_results[model_name] = serializer.data

                                        # Construct the API response with search results
                                        api_response = {
                                                  "status": "success",
                                                  "code": status.HTTP_200_OK,
                                                  "message": f"Search results for '{search_term}'",
                                                  "total_records": total_records,
                                                  "data": serialized_results,
                                        }
                              else:
                                        # No records found for the search term
                                        api_response = {
                                                  "status": "success",
                                                  "code": status.HTTP_200_OK,
                                                  "message": f"No records found for '{search_term}'",
                                                  "total_records": total_records,
                                                  "data": {},
                                        }

                              return Response(api_response, status=status.HTTP_200_OK)

                    except Exception as e:
                              error_message = f"An error occurred while searching: {str(e)}"
                              error_response = {
                                        "status": "error",
                                        "code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                                        "message": error_message,
                              }
                              return Response(error_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

          def filter_model_by_search_term(self, model, search_term):
                    # Convert search term to lowercase
                    search_term = search_term.lower()

                    # Construct a filter condition dynamically for each model
                    filter_conditions = reduce(operator.or_,
                                               [Q(**{f"{field.name}__icontains": search_term}) for field in
                                                model._meta.fields if
                                                isinstance(field, (CharField, TextField))])

                    # Apply the filter condition to the model queryset
                    return model.objects.filter(filter_conditions)

          def get_serializer_class_for_model(self, model_name):
                    # Define mapping between model names and serializer classes
                    serializer_mapping = {
                              'Events': EventSerializer,
                              'Products': ProductSerializer,
                              'User': UserSerializer,
                              # Add mappings for other models as needed
                    }
                    serializer_class = serializer_mapping.get(model_name)
                    if serializer_class is None:
                              print(f"No serializer class found for model: {model_name}")
                    return serializer_class

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
                              serializer = self.get_serializer(data=request.data,
                                                               context={'include_array_fields': True})
                              serializer.is_valid(raise_exception=True)
                              instance = serializer.save()

                              # Check if 'image' field is present in the request data
                              if 'image' in request.data:
                                        # Get the uploaded image instance
                                        if instance.utypeartist == 1:
                                                  uploaded_image = instance.aprofilephoto
                                        else:
                                                  uploaded_image = instance.oprofilephoto

                                        # Get the current file path
                                        current_file_path = uploaded_image.path

                                        # Specify the new file name
                                        new_file_name = f'user_{instance.uid}.png'

                                        # Create the new file path
                                        new_file_path = os.path.join(os.path.dirname(current_file_path), new_file_name)

                                        # Create the directory if it doesn't exist
                                        directory = os.path.dirname(new_file_path)
                                        if not os.path.exists(directory):
                                                  os.makedirs(directory)

                                        # Check if the file exists before renaming
                                        if os.path.exists(current_file_path):
                                                  # Rename the file using the correct new file path
                                                  os.rename(current_file_path, new_file_path)

                                                  # Update the instance with the new file name (relative path)
                                                  if instance.utypeartist == 1:
                                                            instance.aprofilephoto.name = os.path.relpath(new_file_path,
                                                                                                          settings.MEDIA_ROOT_PROFILE)
                                                  else:
                                                            instance.oprofilephoto.name = os.path.relpath(new_file_path,
                                                                                                          settings.MEDIA_ROOT_PROFILE)
                                        else:
                                                  raise FileNotFoundError(
                                                            f"The file '{current_file_path}' does not exist.")

                              # Update the instance in the database with the new file name
                              instance.save()

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
                              serializer = self.get_serializer(instance, data=request.data)
                              serializer.is_valid(raise_exception=True)

                              # Check and update profile photos if present in the request data
                              if 'aprofilephoto' in request.data and request.data['aprofilephoto'] != "":
                                        instance.aprofilephoto = request.data['aprofilephoto']
                              if 'oprofilephoto' in request.data and request.data['oprofilephoto'] != "":
                                        instance.oprofilephoto = request.data['oprofilephoto']

                              # Save the instance after updating
                              instance.save()

                              return Response({'status': 'success', 'message': 'User updated successfully',
                                               'updated_user': serializer.data})
                    except Exception as e:
                              error_msg = 'Failed to update: {}'.format(str(e))
                              error_response = {'status': 'error', 'message': error_msg}
                              return Response(error_response, status=status.HTTP_400_BAD_REQUEST)

          def partial_update(self, request, *args, **kwargs):
                    try:
                              with transaction.atomic():
                                        instance = self.get_object()
                                        serializer = self.get_serializer(instance, data=request.data, partial=True,
                                                                         context={'include_array_fields': True})
                                        serializer.is_valid(raise_exception=True)
                                        instance = serializer.save()

                                        # Check if 'image' field is present in the request data
                                        if 'image' in request.data:
                                                  # Get the uploaded image instance
                                                  uploaded_image = instance.aprofilephoto if instance.utypeartist == 1 else instance.oprofilephoto

                                                  # Get the current file path
                                                  current_file_path = uploaded_image.path

                                                  # Specify the new file name
                                                  new_file_name = f'user_{instance.uid}.png'

                                                  # Create the new file path
                                                  new_file_path = os.path.join(os.path.dirname(current_file_path),
                                                                               new_file_name)

                                                  # Rename the file
                                                  os.rename(current_file_path, new_file_path)

                                                  # Update the instance with the new file name
                                                  uploaded_image.name = new_file_name

                                                  # Update other fields as needed

                                                  # Save the instance
                                                  instance.save()

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
                              serializer = self.get_serializer(artists, many=True,
                                                               context={'include_array_fields': True})
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
                              serializer = self.get_serializer(organizers, many=True,
                                                               context={'include_array_fields': True})
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
                              uemail = serializer.validated_data.get('uemail')
                              upassword = serializer.validated_data.get('upassword')

                              try:
                                        user = User.objects.get(uemail=uemail)

                                        if user.upassword == upassword:
                                                  user_type = None

                                                  if user.utypeartist == serializer.validated_data.get('utypeartist',
                                                                                                       False):
                                                            if user.utypeorganizer == serializer.validated_data.get(
                                                                      'utypeorganizer', False):
                                                                      if user.utypeuser == serializer.validated_data.get(
                                                                                'utypeuser', False):
                                                                                if user.utypeartist:
                                                                                          user_type = 'artist'
                                                                                          user_status = user.artiststatus
                                                                                elif user.utypeorganizer:
                                                                                          user_type = 'organizer'
                                                                                          user_status = user.organizerstatus
                                                                                elif user.utypeuser:
                                                                                          user_type = 'user'
                                                                                          user_status = user.userstatus

                                                                                return Response(
                                                                                          {'message': 'Valid User',
                                                                                           'user_type': user_type,
                                                                                           'user_id': user.uid,
                                                                                           'status': user_status,
                                                                                           'name': user.uname,
                                                                                           'email': user.uemail,
                                                                                           'contact': user.uwhatsappno},
                                                                                          status=status.HTTP_200_OK)
                                                                      else:
                                                                                return Response({
                                                                                          'message': 'Invalid usertype'},
                                                                                          status=status.HTTP_401_UNAUTHORIZED)
                                                            else:
                                                                      return Response(
                                                                                {'message': 'Invalid organizertype'},
                                                                                status=status.HTTP_401_UNAUTHORIZED)
                                                  else:
                                                            return Response({'message': 'Invalid artisttype'},
                                                                            status=status.HTTP_401_UNAUTHORIZED)
                                        else:
                                                  return Response({'message': 'Invalid Password'},
                                                                  status=status.HTTP_401_UNAUTHORIZED)
                              except User.DoesNotExist:
                                        return Response({'message': 'Invalid Credentials'},
                                                        status=status.HTTP_401_UNAUTHORIZED)

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
                              'message': 'Invalid category or subcategory provided for artist.',
                              'data': []
                    }
                    return Response(response_data)

class OrganizerByCategoryAPI(generics.ListAPIView):
          serializer_class = UserSerializer

          def list(self, request, *args, **kwargs):
                    bcategory = self.kwargs.get('businesscategory')
                    category_obj = Businesscategories.objects.filter(businesscategory=bcategory).first()

                    if category_obj:
                              organisers = User.objects.filter(utypeorganizer=1, obusinesscategory=bcategory)
                              serializer = self.get_serializer(organisers, many=True)
                              data = serializer.data
                              response_data = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'Organisers fetched successfully',
                                        'organiserbycategory': data
                              }
                              return Response(response_data)

                    response_data = {
                              'status': 'error',
                              'code': status.HTTP_400_BAD_REQUEST,
                              'message': 'Invalid category provided for organiser.',
                              'data': []
                    }
                    return Response(response_data)

class getWishlistAPI(APIView):
          def get(self, request, uid):
                    try:
                              user = User.objects.get(uid=uid)
                    except User.DoesNotExist:
                              return Response({'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

                    if user.utypeartist == 1:
                              wishlist = user.awishlist.split(',')
                    elif user.utypeorganizer == 1:
                              wishlist = user.owishlist.split(',')
                    else:
                              wishlist = user.uwishlist.split(',')

                    return Response({'wishlist': wishlist}, status=status.HTTP_200_OK)

class addToWishlist(APIView):
          def post(self, request, uid, wished_user_id):
                    try:
                              user = User.objects.get(uid=uid)
                    except User.DoesNotExist:
                              return Response({'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

                    # Function to normalize the wishlist
                    def normalize_wishlist(wishlist_str):
                              if not wishlist_str:
                                        return []
                              return wishlist_str.split(',')

                    # Normalize the wishlist
                    if user.utypeartist == 1:
                              wishlist = normalize_wishlist(user.awishlist)
                    elif user.utypeorganizer == 1:
                              wishlist = normalize_wishlist(user.owishlist)
                    else:
                              wishlist = normalize_wishlist(user.uwishlist)

                    # Convert wished_user_id to string
                    wished_user_id_str = str(wished_user_id)

                    # Check if wished_user_id is already present in the wishlist
                    if wished_user_id_str in wishlist:
                              return Response({'message': 'ID is already present in the wishlist'},
                                              status=status.HTTP_400_BAD_REQUEST)

                    # Add the wished user ID to the wishlist
                    wishlist.append(wished_user_id_str)

                    # Convert the wishlist back to a string representation with commas
                    updated_wishlist = ','.join(wishlist)

                    # Update the corresponding wishlist field in the user object
                    if user.utypeartist == 1:
                              user.awishlist = updated_wishlist
                    elif user.utypeorganizer == 1:
                              user.owishlist = updated_wishlist
                    else:
                              user.uwishlist = updated_wishlist

                    # Save the user object
                    user.save()

                    return Response({'message': 'User added to wishlist successfully'}, status=status.HTTP_201_CREATED)

class deleteFromWishlist(APIView):
          def delete(self, request, uid, wished_user_id):
                    try:
                              user = User.objects.get(uid=uid)
                    except User.DoesNotExist:
                              return Response({'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

                    # Function to normalize the wishlist
                    def normalize_wishlist(wishlist_str):
                              if not wishlist_str:
                                        return []
                              return wishlist_str.split(',')

                    # Normalize the wishlist
                    if user.utypeartist == 1:
                              wishlist = normalize_wishlist(user.awishlist)
                    elif user.utypeorganizer == 1:
                              wishlist = normalize_wishlist(user.owishlist)
                    else:
                              wishlist = normalize_wishlist(user.uwishlist)

                    # Convert wished_user_id to string
                    wished_user_id_str = str(wished_user_id)

                    # Check if wished_user_id is not present in the wishlist
                    if wished_user_id_str not in wishlist:
                              return Response({'message': 'ID not found for deletion'},
                                              status=status.HTTP_400_BAD_REQUEST)

                    # Remove the wished user ID from the wishlist
                    wishlist.remove(wished_user_id_str)

                    # Convert the wishlist back to a string representation with commas
                    updated_wishlist = ','.join(wishlist)

                    # Update the corresponding wishlist field in the user object
                    if user.utypeartist == 1:
                              user.awishlist = updated_wishlist
                    elif user.utypeorganizer == 1:
                              user.owishlist = updated_wishlist
                    else:
                              user.uwishlist = updated_wishlist

                    # Save the user object
                    user.save()

                    return Response({'message': 'User removed from wishlist successfully'}, status=status.HTTP_200_OK)

class getLikesAPI(APIView):
          def get(self, request, uid):
                    try:
                              user = User.objects.get(uid=uid)
                    except User.DoesNotExist:
                              return Response({'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

                    # Function to normalize the likes list
                    def normalize_likes(likes_str):
                              if not likes_str:
                                        return []
                              return likes_str.split(',')

                    # Normalize the likes list
                    if user.utypeartist == 1:
                              likes_list = normalize_likes(user.alikes)
                    elif user.utypeorganizer == 1:
                              likes_list = normalize_likes(user.olikes)
                    else:
                              likes_list = normalize_likes(user.ulikes)

                    # Count the number of likes
                    likes_count = len(likes_list)

                    return Response({'likes': likes_count}, status=status.HTTP_200_OK)

class addToLikes(APIView):
          def post(self, request, uid, liked_user_id):
                    try:
                              user = User.objects.get(uid=uid)
                              liked_user = User.objects.get(uid=liked_user_id)
                    except User.DoesNotExist:
                              return Response({'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

                    # Determine the likes field based on the user's type
                    if user.utypeartist == 1:
                              likes_field = 'alikes'
                    elif user.utypeorganizer == 1:
                              likes_field = 'olikes'
                    else:
                              likes_field = 'ulikes'

                    # Retrieve the current likes list
                    likes_list = getattr(liked_user, likes_field).split(',') if getattr(liked_user, likes_field) else []

                    # Convert liked_user_id to string
                    liked_user_id_str = str(uid)

                    # Check if liked_user_id is already present in the likes list
                    if liked_user_id_str in likes_list:
                              return Response({'message': 'ID is already present in the list'},
                                              status=status.HTTP_400_BAD_REQUEST)

                    # Add the liked user ID to the likes list
                    likes_list.append(liked_user_id_str)

                    # Convert the likes list back to a string representation with commas
                    updated_likes = ','.join(likes_list)

                    # Update the likes field of the liked user
                    setattr(liked_user, likes_field, updated_likes)
                    liked_user.save()

                    return Response({'message': 'User added to likes successfully'}, status=status.HTTP_201_CREATED)

class deleteFromLikes(APIView):
          def delete(self, request, uid, liked_user_id):
                    try:
                              user = User.objects.get(uid=uid)
                    except User.DoesNotExist:
                              return Response({'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

                    # Check if the user exists in the liked user's likes list
                    liked_user = User.objects.filter(uid=liked_user_id)
                    if not liked_user.exists():
                              return Response({'message': 'Liked user does not exist'},
                                              status=status.HTTP_404_NOT_FOUND)

                    # Function to normalize the likes list
                    def normalize_likes(likes_str):
                              if not likes_str:
                                        return []
                              return likes_str.split(',')

                    # Normalize the likes list based on user type
                    if user.utypeartist == 1:
                              likes_field = 'alikes'
                    elif user.utypeorganizer == 1:
                              likes_field = 'olikes'
                    else:
                              likes_field = 'ulikes'

                    # Check if the user's ID is in the liked user's likes list
                    liked_user = liked_user.first()
                    liked_user_likes = normalize_likes(getattr(liked_user, likes_field))
                    user_id_str = str(uid)

                    if user_id_str not in liked_user_likes:
                              return Response({'message': 'Your ID is not in the liked user\'s likes list'},
                                              status=status.HTTP_400_BAD_REQUEST)

                    # Remove the user's ID from the liked user's likes list
                    liked_user_likes.remove(user_id_str)
                    updated_likes = ','.join(liked_user_likes)

                    # Update the corresponding likes field in the liked user's object
                    setattr(liked_user, likes_field, updated_likes)
                    liked_user.save()

                    return Response({'message': 'You have been removed from the liked user\'s likes list'},
                                    status=status.HTTP_200_OK)

class UserCountAPI(generics.ListAPIView):
          serializer_class = UserSerializer

          def list(self, request, *args, **kwargs):
                    try:
                              total_users = User.objects.count()
                              artists = User.objects.filter(utypeartist=1).count()
                              organizers = User.objects.filter(utypeorganizer=1).count()
                              users = User.objects.filter(utypeuser=1).count()
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'Total count of all users',
                                        'total_count': total_users,
                                        'artists': artists,
                                        'organizers': organizers,
                                        'users': users,
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

class AddCarouselImages(APIView):
          serializer_class = CarouselSerializer

          def post(self, request, *args, **kwargs):
                    serializer = self.serializer_class(data=request.data)

                    if serializer.is_valid():
                              # Retrieve image fields from serializer data
                              images = [serializer.validated_data.get(f'image{i}') for i in range(1, 6)]

                              # Specify the folder path for storing image files
                              folder_name_carousel = 'carousel_images'
                              folder_path_carousel = os.path.join(settings.MEDIA_ROOT_CAROUSEL, folder_name_carousel)
                              os.makedirs(folder_path_carousel, exist_ok=True)

                              saved_file_paths = []
                              for index, base64_code in enumerate(images):
                                        if base64_code is None:
                                                  continue  # Skip empty fields

                                        image_name = f'image{index + 1}.png'  # Change the extension based on your requirements
                                        save_path = os.path.join(folder_path_carousel, image_name)

                                        try:
                                                  # Write the base64 code to the file
                                                  with open(save_path, 'wb') as image_file:
                                                            image_file.write(base64.b64decode(base64_code))
                                        except Exception as e:
                                                  # Handle file writing errors
                                                  error_message = f'Error saving image {index}: {str(e)}'
                                                  return Response({'error': error_message},
                                                                  status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                                        except RequestDataTooBig:
                                                  # Handle RequestDataTooBig error
                                                  return Response({'error': 'Request body exceeded maximum size.'},
                                                                  status=413)

                                        saved_file_paths.append(save_path)

                              response_data = {
                                        'status': 'success',
                                        'code': status.HTTP_201_CREATED,
                                        'message': 'Base64 codes converted to images successfully',
                                        'saved_file_paths': saved_file_paths
                              }
                              return Response(response_data)

                    return Response(serializer.errors)

class GetCarouselImages(APIView):
          def get(self, request, *args, **kwargs):
                    # Specify the folder path where images are stored
                    folder_name_carousel = 'carousel_images'
                    folder_path_carousel = os.path.join(settings.MEDIA_ROOT_CAROUSEL, folder_name_carousel)

                    # Check if the folder exists
                    if not os.path.exists(folder_path_carousel):
                              return Response({'error': 'Image folder not found'}, status=status.HTTP_404_NOT_FOUND)

                    # Get a list of image files in the folder and sort them
                    image_files = os.listdir(folder_path_carousel)
                    image_files.sort()  # Sort the list of filenames

                    # Initialize a dictionary to store base64 encoded strings of images with their corresponding filenames
                    image_data = {}

                    # Loop through each image file, read its contents, and encode it in base64
                    for image_file in image_files:
                              image_path = os.path.join(folder_path_carousel, image_file)
                              try:
                                        with open(image_path, 'rb') as f:
                                                  image_bytes = f.read()
                                                  image_base64 = base64.b64encode(image_bytes).decode('utf-8')
                                                  image_data[image_file] = image_base64
                              except Exception as e:
                                        # Handle file reading errors
                                        error_message = f'Error reading image {image_file}: {str(e)}'
                                        return Response({'error': error_message},
                                                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

                    # Return the dictionary containing filenames and their corresponding base64 encoded image strings
                    response_data = {
                              'status': 'success',
                              'code': status.HTTP_200_OK,
                              'base64images': image_data,
                    }
                    return Response(response_data)

# class AddProfilePhoto(APIView):
#           serializer_class = ProfilePhotoSerializer
#
#           def post(self, request, *args, **kwargs):
#                     serializer = self.serializer_class(data=request.data)
#
#                     if serializer.is_valid():
#                               user_id = serializer.validated_data.get('userid')
#                               photo_base64 = serializer.validated_data.get('photo')
#
#                               # Specify the folder path for storing profile photos
#                               folder_name_profile = 'profile_photos'
#                               folder_path_profile = os.path.join(settings.MEDIA_ROOT_PROFILE, folder_name_profile)
#                               os.makedirs(folder_path_profile, exist_ok=True)
#
#                               photo_name = f'profile_photo_{user_id}.png'  # Or any desired extension
#
#                               try:
#                                         # Write the base64 code to the file
#                                         with open(os.path.join(folder_path_profile, photo_name), 'wb') as photo_file:
#                                                   photo_file.write(base64.b64decode(photo_base64))
#                               except Exception as e:
#                                         # Handle file writing errors
#                                         error_message = f'Error saving profile photo: {str(e)}'
#                                         return Response({'error': error_message},
#                                                         status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#                               response_data = {
#                                         'status': 'success',
#                                         'code': status.HTTP_201_CREATED,
#                                         'message': 'Profile photo uploaded successfully',
#                                         'photo_path': os.path.join(folder_path_profile, photo_name)
#                               }
#                               return Response(response_data)
#
#                     return Response(serializer.errors)

class GetProfilePhoto(APIView):
          serializer_class = ProfilePhotoSerializer

          def get(self, request, *args, **kwargs):
                    userid = self.kwargs.get('uid')

                    if not userid:
                              return Response({'error': 'User ID is required'}, status=status.HTTP_400_BAD_REQUEST)

                    try:
                              user_instance = User.objects.get(uid=userid)
                    except User.DoesNotExist:
                              return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

                    if user_instance.utypeartist == 1:
                              profile_photo = user_instance.aprofilephoto
                    else:
                              profile_photo = user_instance.oprofilephoto

                    if not profile_photo:
                              return Response({'error': 'Profile photo not found'}, status=status.HTTP_404_NOT_FOUND)

                    # Use PIL to determine content type
                    image = Image.open(profile_photo.path)
                    content_type = f'image/{image.format.lower()}'

                    # Return the profile photo as HttpResponse
                    with open(profile_photo.path, 'rb') as image_file:
                              return HttpResponse(image_file.read(), content_type=content_type)

class AddMultiplePhotos(APIView):
          serializer_class = MultiplePhotosSerializer
          max_photos_per_user = 10

          def post(self, request, *args, **kwargs):
                    serializer = self.serializer_class(data=request.data)

                    if serializer.is_valid():
                              user_id = serializer.validated_data.get('userid')
                              photos_base64 = {int(key[5:]): value for key, value in serializer.validated_data.items()
                                               if key.startswith('image')}

                              if not photos_base64:
                                        return Response({'error': 'At least one image must be provided'},
                                                        status=status.HTTP_400_BAD_REQUEST)

                              # Specify the folder path for storing user photos
                              folder_name_multiple = f'user_{user_id}_photos'
                              folder_path_multiple = os.path.join(settings.MEDIA_ROOT_MULTIPLE, folder_name_multiple)
                              os.makedirs(folder_path_multiple, exist_ok=True)

                              saved_file_paths = []
                              for field_number, photo_base64 in photos_base64.items():
                                        photo_name = f'photo_{field_number}.png'  # Correctly number the photo based on the field number
                                        save_path = os.path.join(folder_path_multiple, photo_name)

                                        try:
                                                  # Write the base64 code to the file
                                                  with open(save_path, 'wb') as photo_file:
                                                            photo_file.write(base64.b64decode(photo_base64))
                                        except Exception as e:
                                                  # Handle file writing errors
                                                  error_message = f'Error saving photo {field_number}: {str(e)}'
                                                  return Response({'error': error_message},
                                                                  status=status.HTTP_500_INTERNAL_SERVER_ERROR)

                                        saved_file_paths.append(save_path)

                              response_data = {
                                        'status': 'success',
                                        'code': status.HTTP_201_CREATED,
                                        'message': 'Photos uploaded successfully',
                                        'saved_file_paths': saved_file_paths
                              }
                              return Response(response_data)

                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetMultiplePhotos(APIView):
          def get(self, request, *args, **kwargs):
                    user_id = self.kwargs.get('userid')

                    if not user_id:
                              return Response({'error': 'User ID is required'}, status=status.HTTP_400_BAD_REQUEST)

                    # Specify the folder path for storing user photos
                    folder_name_multiple = f'user_{user_id}_photos'
                    folder_path_multiple = os.path.join(settings.MEDIA_ROOT_MULTIPLE, folder_name_multiple)

                    if not os.path.exists(folder_path_multiple):
                              return Response({'error': 'Photos not found for this user'},
                                              status=status.HTTP_404_NOT_FOUND)

                    # Get a list of image files in the folder
                    image_files = os.listdir(folder_path_multiple)

                    # Initialize a dictionary to store base64 encoded strings of images with their corresponding filenames
                    image_data = {}

                    # Loop through each image file and read its contents
                    for image_file in image_files:
                              image_path = os.path.join(folder_path_multiple, image_file)
                              try:
                                        # Read the image file and encode it in base64
                                        with open(image_path, 'rb') as f:
                                                  image_bytes = f.read()
                                                  image_base64 = base64.b64encode(image_bytes).decode('utf-8')
                                                  image_data[image_file] = image_base64
                              except Exception as e:
                                        # Handle file reading errors
                                        error_message = f'Error reading image {image_file}: {str(e)}'
                                        return Response({'error': error_message},
                                                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

                    # Return the dictionary containing filenames and their corresponding base64 encoded image strings
                    response_data = {
                              'status': 'success',
                              'code': status.HTTP_200_OK,
                              'base64images': image_data,
                    }
                    return Response(response_data)

class SendMessageAPI(APIView):
          def post(self, request):
                    subject = request.data.get('subject', '')
                    sender_email = request.data.get('email', '')
                    message = request.data.get('message', '')

                    # Adding sender's email address to the message content
                    if sender_email:
                              message = f'From : {sender_email}' + f'\n\nMessage : {message}'

                    if not subject or not sender_email or not message:
                              return Response({'error': 'Subject, email, and message are required.'},
                                              status=status.HTTP_400_BAD_REQUEST)

                    recipient_email = 'prajwalpunekar9565@gmail.com'  # Your email address
                    try:
                              send_mail(subject, message, sender_email, [recipient_email])
                              response_data = {'success': 'Message sent successfully.'}
                              status_code = status.HTTP_200_OK
                    except Exception as e:
                              response_data = {'error': str(e)}
                              status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

                    return Response(response_data, status=status_code)
