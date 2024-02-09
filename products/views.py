from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from products.models import Products
from products.serializers import ProductSerializer

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
                                        'message': 'ALL Products',
                                        'all_products': serializer.data,
                              }
                              return Response(api_response, status=status.HTTP_200_OK)
                    except Exception as e:
                              error_message = 'An error occurred while fetching product: {}'.format(str(e))
                    error_response = {
                              'status': 'error',
                              'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                              'message': error_message
                    }
                    return Response(error_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
                              return Response(api_response, status=status.HTTP_200_OK)
                    except Exception as e:
                              error_message = 'An error occurred while fetching product: {}'.format(str(e))
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                                        'message': error_message
                              }
                    return Response(error_response, status=status.HTTP_404_NOT_FOUND)

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
                    return Response(error_response, status=status.HTTP_400_BAD_REQUEST)

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
