import os
import base64
from django.conf import settings
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from products.models import Products
from products.serializers import ProductSerializer, ProductPhotoSerializer

# Create your views here.
class ProductsAPI(ModelViewSet):
          queryset = Products.objects.all()
          serializer_class = ProductSerializer

          def list(self, request, *args, **kwargs):
                    try:
                              product = Products.objects.all()
                              serializer = self.get_serializer(product, many=True)
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'All Products',
                                        'all_products': serializer.data,
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_message = 'An error occurred while fetching product: {}'.format(str(e))
                    error_response = {
                              'status': 'error',
                              'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                              'message': error_message
                    }
                    return Response(error_response)

          def retrieve(self, request, *args, **kwargs):
                    try:
                              instance = self.get_object()
                              serializer = self.get_serializer(instance)
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'Products details fetched successfully',
                                        'product_details': serializer.data,
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_message = 'An error occurred while fetching product: {}'.format(str(e))
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                                        'message': error_message
                              }
                    return Response(error_response)

          def create(self, request, *args, **kwargs):
                    try:
                              serializer = self.get_serializer(data=request.data)
                              serializer.is_valid(raise_exception=True)
                              serializer.save()
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_201_CREATED,
                                        'message': 'Product details added successfully',
                                        'new_product': serializer.data,
                              }
                              return Response(api_response, status=status.HTTP_201_CREATED)
                    except Exception as e:
                              error_message = 'Failed to add product details:{}'.format(str(e))
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_400_BAD_REQUEST,
                                        'message': error_message
                              }
                    return Response(error_response)

          def update(self, request, *args, **kwargs):
                    try:
                              instance = self.get_object()
                              serializer = self.get_serializer(instance, data=request.data)
                              serializer.is_valid(raise_exception=True)
                              serializer.save()
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'Product updated successfully',
                                        'updated_product': serializer.data,
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_message = 'Failed to update product details:{}'.format(str(e))
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_400_BAD_REQUEST,
                                        'message': error_message
                              }
                    return Response(error_response)

          def partial_update(self, request, *args, **kwargs):
                    try:
                              instance = self.get_object()
                              serializer = self.get_serializer(instance, data=request.data, partial=True)
                              serializer.is_valid(raise_exception=True)
                              serializer.save()
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'Product updated successfully',
                                        'updated_product': serializer.data,
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_message = 'Failed to partially update product details:{}'.format(str(e))
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_400_BAD_REQUEST,
                                        'message': error_message
                              }
                    return Response(error_response)

          def destroy(self, request, *args, **kwargs):
                    try:
                              instance = self.get_object()
                              instance.delete()

                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'Product deleted successfully',
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_message = 'Failed to delete product details:{}'.format(str(e))
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_400_BAD_REQUEST,
                                        'message': error_message
                              }
                    return Response(error_response)

class AddProductPhoto(APIView):
          serializer_class = ProductPhotoSerializer

          def post(self, request, *args, **kwargs):
                    serializer = self.serializer_class(data=request.data)

                    if serializer.is_valid():
                              product_id = serializer.validated_data.get('productid')
                              photo_base64 = serializer.validated_data.get('photo')

                              # Specify the folder path for storing profile photos
                              folder_name_product = 'product_photos'
                              folder_path_product = os.path.join(settings.MEDIA_ROOT_PRODUCT, folder_name_product)
                              os.makedirs(folder_path_product, exist_ok=True)

                              photo_name = f'product_photo_{product_id}.png'  # Or any desired extension

                              try:
                                        # Write the base64 code to the file
                                        with open(os.path.join(folder_path_product, photo_name), 'wb') as photo_file:
                                                  photo_file.write(base64.b64decode(photo_base64))
                              except Exception as e:
                                        # Handle file writing errors
                                        error_message = f'Error saving product photo: {str(e)}'
                                        return Response({'error': error_message},
                                                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

                              response_data = {
                                        'status': 'success',
                                        'code': status.HTTP_201_CREATED,
                                        'message': 'Product photo uploaded successfully',
                                        'photo_path': os.path.join(folder_path_product, photo_name)
                              }
                              return Response(response_data)

                    return Response(serializer.errors)

class GetProductPhoto(APIView):
          serializer_class = ProductPhotoSerializer

          def get(self, request, *args, **kwargs):
                    product_id = self.kwargs.get('productid')

                    if not product_id:
                              return Response({'error': 'Product ID is required'}, status=status.HTTP_400_BAD_REQUEST)

                    # Specify the folder path where profile photos are stored
                    folder_name_product = 'product_photos'
                    folder_path_product = os.path.join(settings.MEDIA_ROOT_PRODUCT, folder_name_product)

                    # Check if the folder exists
                    if not os.path.exists(folder_path_product):
                              return Response({'error': 'Product photo folder not found'},
                                              status=status.HTTP_404_NOT_FOUND)

                    photo_name = f'product_photo_{product_id}.png'  # Or any desired extension
                    photo_path = os.path.join(folder_path_product, photo_name)

                    # Check if the photo exists
                    if not os.path.exists(photo_path):
                              return Response({'error': 'Product photo not found'}, status=status.HTTP_404_NOT_FOUND)

                    try:
                              # Read the profile photo file and encode it in base64
                              with open(photo_path, 'rb') as f:
                                        photo_bytes = f.read()
                                        photo_base64 = base64.b64encode(photo_bytes).decode('utf-8')
                    except Exception as e:
                              # Handle file reading errors
                              error_message = f'Error reading product photo: {str(e)}'
                              return Response({'error': error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

                    response_data = {
                              'status': 'success',
                              'code': status.HTTP_200_OK,
                              'base64_photo': photo_base64,
                    }
                    return Response(response_data)
