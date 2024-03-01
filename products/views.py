import os
import base64
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
                              serializer = self.get_serializer(data=request.data)
                              serializer.is_valid(raise_exception=True)
                              # Save the product details
                              instance = serializer.save()

                              # Ensure instance has been saved and has a valid ID (pid)
                              if instance.pid:
                                        # Handle file upload separately
                                        photo = request.FILES.get('pimages')
                                        if photo:
                                                  # Construct the file path
                                                  filename = f'product_{instance.pid}.png'
                                                  file_path = os.path.join(settings.MEDIA_ROOT_PRODUCT, filename)

                                                  # Create the directory if it doesn't exist
                                                  os.makedirs(settings.MEDIA_ROOT_PRODUCT, exist_ok=True)

                                                  # Write the image data to the file
                                                  with open(file_path, 'wb') as image_file:
                                                            for chunk in photo.chunks():
                                                                      image_file.write(chunk)

                                                  # Update the instance with the relative file path
                                                  instance.pimages = os.path.join(settings.MEDIA_URL_PRODUCT, filename)
                                                  instance.save()
                                        else:
                                                  raise ValueError("No photo data found in the request.")
                              else:
                                        raise ValueError("Failed to retrieve product ID.")

                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_201_CREATED,
                                        'message': 'Product details added successfully',
                                        'new_product': serializer.data,
                              }
                              return Response(api_response, status=status.HTTP_201_CREATED)
                    except Exception as e:
                              error_message = 'Failed to add product details: {}'.format(str(e))
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
                              photo = serializer.validated_data.get('photo')

                              # Create the directory if it doesn't exist
                              if not os.path.exists(settings.MEDIA_ROOT_PRODUCT):
                                        os.makedirs(settings.MEDIA_ROOT_PRODUCT, exist_ok=True)

                              # Check if there is an existing photo for the product
                              try:
                                        product_instance = Products.objects.get(pid=product_id)
                                        if product_instance.pimages:
                                                  # If there's an existing photo, delete it
                                                  product_instance.pimages.delete()
                              except Products.DoesNotExist:
                                        # If the product doesn't exist, return an error
                                        return Response({'error': 'Product not found'},
                                                        status=status.HTTP_404_NOT_FOUND)

                              # Construct the file name using the product ID
                              file_name = f'product_{product_id}.png'  # Or any desired extension
                              # Construct the full file path including the directory and the file name
                              file_path = os.path.join(settings.MEDIA_ROOT_PRODUCT, file_name)
                              # Save the image to the specified file path
                              product_instance.pimages.save(file_path, photo, save=True)

                              response_data = {
                                        'status': 'success',
                                        'code': status.HTTP_201_CREATED,
                                        'message': 'Product photo uploaded successfully',
                                        'photo_url': os.path.join(settings.MEDIA_URL_PRODUCT, file_name)
                              }
                              return Response(response_data)

                    return Response(serializer.errors)

class GetProductPhoto(APIView):
          serializer_class = ProductPhotoSerializer

          def get(self, request, *args, **kwargs):
                    product_id = self.kwargs.get('productid')

                    if not product_id:
                              return Response({'error': 'Product ID is required'}, status=status.HTTP_400_BAD_REQUEST)

                    try:
                              product_instance = Products.objects.get(pid=product_id)
                    except Products.DoesNotExist:
                              return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

                    if not product_instance.pimages:
                              return Response({'error': 'Product photo not found'}, status=status.HTTP_404_NOT_FOUND)

                    image_path = product_instance.pimages.path

                    # Read the image file and return it as HttpResponse
                    with open(image_path, 'rb') as image_file:
                              return HttpResponse(image_file.read(),
                                                  content_type='image/png')  # Adjust content type as needed
