import os
import base64
from django.core.exceptions import RequestDataTooBig
from django.conf import settings
from django.db.models import Max, Count
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from users.models import User
from artistcategories.models import Artistcategories
from users.serializers import UserSerializer, UserLoginSerializer, CarouselSerializer
from artistcategories.serializers import ArtistcategoriesSerializer
from businesscategories.models import Businesscategories
from django.db.models import Q

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
                  search_term = request.query_params.get('search_term')
                  if not search_term:
                      return Response({"message": "Please provide a search term"}, status=status.HTTP_400_BAD_REQUEST)

                  # Perform case-insensitive search by name or mobile number
                  search_results = User.objects.filter(Q(uname=search_term))

                  # Extract start index and limit from the request query parameters
                  start_index = int(request.query_params.get('start_index', 0))
                  limit = 50  # Default limit is 50

                  # Ensure ordering by primary key for consistent pagination
                  search_results = search_results.order_by('pk')

                  # Use Django Paginator to get the subset of records
                  paginator = Paginator(search_results, limit)
                  page_number = (start_index // limit) + 1  # Calculate page number based on starting index

                  try:
                      paginated_search_results = paginator.page(page_number)
                  except PageNotAnInteger:
                      paginated_search_results = paginator.page(1)
                  except EmptyPage:
                      return Response({"message": "No more records available"}, status=status.HTTP_200_OK)

                  serializer = self.get_serializer(paginated_search_results, many=True)

                  api_response = {
                      "status": "success",
                      "code": status.HTTP_200_OK,
                      "message": f"Search results for '{search_term}'",
                      "start_index": start_index,
                      "limit": limit,
                      "total_records": paginator.count,
                      "data": serializer.data,
                  }
                  return Response(api_response, status=status.HTTP_200_OK)
              except Exception as e:
                  error_message = (
                      "An error occurred while searching user: {}".format(str(e))
                  )
                  error_response = {
                      "status": "error",
                      "code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                      "message": error_message,
                  }
                  return Response(
                      error_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR
                  )

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
                              'message': 'Invalid category or subcategory provided for artist.',
                              'data': []
                    }
                    return Response(response_data)

class OrganiserByCategoryAPI(generics.ListAPIView):
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
            return Response({"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

        if user.utypeartist == 1:
            wishlist = user.awishlist.split(',')
        elif user.utypeorganizer == 1:
            wishlist = user.owishlist.split(',')
        else:
            wishlist = user.uwishlist.split(',')

        return Response({"wishlist": wishlist}, status=status.HTTP_200_OK)

class addToWishlist(APIView):
    def post(self, request, uid, wished_user_id):
        try:
            user = User.objects.get(uid=uid)
        except User.DoesNotExist:
            return Response({"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

        if user.utypeartist == 1:
            user.awishlist += f",{wished_user_id}"
        elif user.utypeorganizer == 1:
            user.owishlist += f",{wished_user_id}"
        else:
            user.uwishlist += f",{wished_user_id}"
        user.save()

        return Response({"message": "User added to wishlist successfully"}, status=status.HTTP_201_CREATED)

class deleteFromWishlist(APIView):
    def delete(self, request, uid, wished_user_id):
        try:
            user = User.objects.get(uid=uid)
        except User.DoesNotExist:
            return Response({"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

        # Split the wishlist string into a list of IDs
        if user.utypeartist == 1:
            wishlist = user.awishlist.split(',')
        elif user.utypeorganizer == 1:
            wishlist = user.owishlist.split(',')
        else:
            wishlist = user.uwishlist.split(',')

        # Convert wished_user_id to the same type as the IDs in the wishlist
        wished_user_id_str = str(wished_user_id)

        # Remove the wished user ID from the wishlist
        if wished_user_id_str in wishlist:
            wishlist.remove(wished_user_id_str)

        # Join the updated wishlist back into a string
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

        return Response({"message": "User removed from wishlist successfully"}, status=status.HTTP_200_OK)

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

class CarouselAPI(APIView):
    serializer_class = CarouselSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            # Retrieve image fields from serializer data
            images = [serializer.validated_data.get(f'image{i}') for i in range(1, 6)]

            # Specify the folder path for storing image files
            folder_name = 'carousel_images'
            folder_path = os.path.join(settings.MEDIA_ROOT, folder_name)
            os.makedirs(folder_path, exist_ok=True)

            saved_file_paths = []
            for index, base64_code in enumerate(images):
                if base64_code is None:
                    continue # Skip empty fields

                image_name = f'image{index + 1}.png'  # Change the extension based on your requirements
                save_path = os.path.join(folder_path, image_name)

                try:
                    # Write the base64 code to the file
                    with open(save_path, 'wb') as image_file:
                        image_file.write(base64.b64decode(base64_code))
                except Exception as e:
                    # Handle file writing errors
                    error_message = f"Error saving image {index}: {str(e)}"
                    return Response({"error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                except RequestDataTooBig:
                          # Handle RequestDataTooBig error
                          return Response({"error": "Request body exceeded maximum size."}, status=413)

                print("images saved")
                saved_file_paths.append(save_path)

            response_data = {
                'status': 'success',
                'code': status.HTTP_201_CREATED,
                'message': 'Base64 codes converted to images successfully',
                'saved_file_paths': saved_file_paths
            }
            return Response(response_data)

        return Response(serializer.errors)


    def get(self, request, *args, **kwargs):
              # Specify the folder path where images are stored
              folder_name = 'carousel_images'
              folder_path = os.path.join(settings.MEDIA_ROOT, folder_name)

              # Check if the folder exists
              if not os.path.exists(folder_path):
                        return Response({"error": "Image folder not found"}, status=status.HTTP_404_NOT_FOUND)

              # Get a list of image files in the folder
              image_files = os.listdir(folder_path)

              # Initialize a dictionary to store base64 encoded strings of images with their corresponding filenames
              image_data = {}

              # Loop through each image file and read its contents
              for image_file in image_files:
                        image_path = os.path.join(folder_path, image_file)
                        try:
                                  # Read the image file and encode it in base64
                                  with open(image_path, 'rb') as f:
                                            image_bytes = f.read()
                                            image_base64 = base64.b64encode(image_bytes).decode('utf-8')
                                            image_data[image_file] = image_base64
                        except Exception as e:
                                  # Handle file reading errors
                                  error_message = f"Error reading image {image_file}: {str(e)}"
                                  return Response({"error": error_message},
                                                  status=status.HTTP_500_INTERNAL_SERVER_ERROR)

              # Return the dictionary containing filenames and their corresponding base64 encoded image strings
              response_data = {
                        'status': 'success',
                        'code': status.HTTP_200_OK,
                        'base64images': image_data,
              }
              return Response(response_data)
