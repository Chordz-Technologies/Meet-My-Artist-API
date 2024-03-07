import os
import base64
from PIL import Image
from io import BytesIO
from django.db import transaction
from django.conf import settings
from django.core.files.base import ContentFile
from django.http import HttpResponse
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
                              serializer = self.serializer_class(data=request.data)
                              serializer.is_valid(raise_exception=True)
                              instance = serializer.save()

                              # Check if 'image' field is present in the request data
                              if 'image' in request.data:
                                        # Get the uploaded image instance
                                        uploaded_image = instance.pimages

                                        # Get the current file path
                                        current_file_path = uploaded_image.path

                                        # Specify the new file name
                                        new_file_name = f'product_{instance.pid}.png'

                                        # Create the new file path
                                        new_file_path = os.path.join(os.path.dirname(current_file_path),
                                                                     new_file_name)

                                        # Delete the old file if it exists
                                        if os.path.exists(new_file_path):
                                                  os.remove(new_file_path)

                                        # Rename the file
                                        os.rename(current_file_path, new_file_path)

                                        # Update the instance with the new file name
                                        instance.pimages.name = new_file_path

                              # Update the instance in the database with the new file name
                              instance.save()

                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_201_CREATED,
                                        'message': 'Product details added successfully',
                                        'new_product': serializer.data,  # Include serialized data in response
                              }
                              return Response(api_response, status=status.HTTP_201_CREATED)
                    except Exception as e:
                              error_message = 'Failed to add product details: {}'.format(str(e))
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_400_BAD_REQUEST,
                                        'message': error_message
                              }
                              return Response(error_response, status=status.HTTP_400_BAD_REQUEST)

          def update(self, request, *args, **kwargs):
                    try:
                              with transaction.atomic():
                                        instance = self.get_object()
                                        serializer = self.get_serializer(instance, data=request.data)
                                        serializer.is_valid(raise_exception=True)
                                        instance = serializer.save()

                                        # Check if 'image' field is present in the request data
                                        if 'image' in request.data:
                                                  # Get the uploaded image instance
                                                  uploaded_image = instance.pimages

                                                  # Get the current file path
                                                  current_file_path = uploaded_image.path

                                                  # Specify the new file name
                                                  new_file_name = f'product_{instance.pid}.png'

                                                  # Create the new file path
                                                  new_file_path = os.path.join(os.path.dirname(current_file_path),
                                                                               new_file_name)

                                                  # Delete the old file if it exists
                                                  if os.path.exists(new_file_path):
                                                            os.remove(new_file_path)

                                                  # Rename the file
                                                  os.rename(current_file_path, new_file_path)

                                                  # Update the instance with the new file name
                                                  instance.pimages.name = new_file_path

                                                  # Update the instance in the database with the new file name
                                                  instance.save()

                                        api_response = {
                                                  'status': 'success',
                                                  'code': status.HTTP_200_OK,
                                                  'message': 'Product updated successfully',
                                                  'updated_product': serializer.data,
                                        }
                                        return Response(api_response, status=status.HTTP_200_OK)
                    except Exception as e:
                              error_message = 'Failed to update product details:{}'.format(str(e))
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_400_BAD_REQUEST,
                                        'message': error_message
                              }
                              return Response(error_response, status=status.HTTP_400_BAD_REQUEST)

          def partial_update(self, request, *args, **kwargs):
                    try:
                              with transaction.atomic():
                                        instance = self.get_object()
                                        serializer = self.get_serializer(instance, data=request.data, partial=True)
                                        serializer.is_valid(raise_exception=True)
                                        instance = serializer.save()

                                        # Check if 'image' field is present in the request data
                                        if 'image' in request.data:
                                                  # Get the uploaded image instance
                                                  uploaded_image = instance.pimages

                                                  # Get the current file path
                                                  current_file_path = uploaded_image.path

                                                  # Specify the new file name
                                                  new_file_name = f'product_{instance.pid}.png'

                                                  # Create the new file path
                                                  new_file_path = os.path.join(os.path.dirname(current_file_path),
                                                                               new_file_name)

                                                  # Delete the old file if it exists
                                                  if os.path.exists(new_file_path):
                                                            os.remove(new_file_path)

                                                  # Rename the file
                                                  os.rename(current_file_path, new_file_path)

                                                  # Update the instance with the new file name
                                                  instance.pimages.name = new_file_path

                                                  # Update the instance in the database with the new file name
                                                  instance.save()

                                        api_response = {
                                                  'status': 'success',
                                                  'code': status.HTTP_200_OK,
                                                  'message': 'Product partially updated successfully',
                                                  'updated_product': serializer.data,
                                        }
                                        return Response(api_response, status=status.HTTP_200_OK)
                    except Exception as e:
                              error_message = 'Failed to partially update product details:{}'.format(str(e))
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_400_BAD_REQUEST,
                                        'message': error_message
                              }
                              return Response(error_response, status=status.HTTP_400_BAD_REQUEST)

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

# class AddProductImage(APIView):
#
#           def post(self, request, *args, **kwargs):
#                     product_id = request.data.get('pid')
#                     product_image = request.FILES.get('pimage')
#
#                     try:
#                               # Retrieve the product instance
#                               product = Products.objects.get(pk=product_id)
#                     except Products.DoesNotExist:
#                               return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
#
#                     # Update the product instance with the uploaded image
#                     product.pimages = product_image
#                     product.save()
#
#                     response_data = {
#                               'status': 'success',
#                               'code': status.HTTP_201_CREATED,
#                               'message': 'Product image uploaded successfully',
#                               'image_path': product.pimages.url  # Get the URL of the uploaded image
#                     }
#                     return Response(response_data, status=status.HTTP_201_CREATED)

class GetProductPhoto(APIView):
          serializer_class = ProductPhotoSerializer

          def get(self, request, *args, **kwargs):
                    productid = self.kwargs.get('pid')

                    if not productid:
                              return Response({'error': 'Product ID is required'},
                                              status=status.HTTP_400_BAD_REQUEST)

                    try:
                              product_instance = Products.objects.get(pid=productid)
                    except Products.DoesNotExist:
                              return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

                    product_photo = product_instance.pimages

                    if not product_photo:
                              return Response({'error': 'Product photo not found'},
                                              status=status.HTTP_404_NOT_FOUND)

                    # Use PIL to determine content type
                    image = Image.open(product_photo.path)
                    content_type = f'image/{image.format.lower()}'

                    # Return the profile photo as HttpResponse
                    with open(product_photo.path, 'rb') as image_file:
                              return HttpResponse(image_file.read(), content_type=content_type)
