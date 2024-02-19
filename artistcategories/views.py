from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from artistcategories.models import Artistcategories
from artistcategories.serializers import ArtistcategoriesSerializer

# Create your views here.
class ArtistcategoriesAPI(ModelViewSet):
          queryset = Artistcategories.objects.all()
          serializer_class = ArtistcategoriesSerializer

          def list(self, request, *args, **kwargs):
                    try:
                              categories = Artistcategories.objects.all()
                              serializer = self.get_serializer(categories, many=True)

                              formatted_data = []
                              for category in serializer.data:
                                        scname = category.get('scname', '')  # Get scname or an empty string if it's None
                                        formatted_category = {
                                                  'cid': category['cid'],
                                                  'cname': category['cname'],
                                                  'scname': [subcategory.strip() for subcategory in
                                                             scname.split(',')] if scname else []
                                        }
                                        formatted_data.append(formatted_category)

                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'All Categories',
                                        'all_categories': formatted_data,
                              }
                              return Response(api_response)

                    except Exception as e:
                              error_message = 'An error occurred while fetching artistcategories: {}'.format(str(e))
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

                              scname_value = serializer.data.get('scname','')  # Get scname or an empty string if it's None
                              formatted_data = {
                                        'cid': serializer.data['cid'],
                                        'cname': serializer.data['cname'],
                                        'scname': [subcategory.strip() for subcategory in
                                                   scname_value.split(',')] if scname_value else []
                              }
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'Category',
                                        'category_details': formatted_data
                              }
                              return Response(api_response)

                    except Exception as e:
                              error_message = 'An error occurred while fetching the category: {}'.format(str(e))
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                                        'message': error_message
                              }
                              return Response(error_response)

          def subcategories_byname(self, request, cname):
                    try:
                              category_instance = Artistcategories.objects.get(cname=cname)
                              serializer = self.get_serializer(category_instance)

                              formatted_data = []
                              # Check if serializer.data is a list
                              if isinstance(serializer.data, list):
                                        for category_data in serializer.data:
                                                  scname = category_data.get('scname', '')
                                                  formatted_category = {
                                                            'cid': category_data['cid'],
                                                            'cname': category_data['cname'],
                                                            'scname': [subcategory.strip() for subcategory in
                                                                       scname.split(',')] if scname else []
                                                  }
                                                  formatted_data.append(formatted_category)
                              else:
                                        # Handle the case when serializer.data is a dictionary
                                        scname = serializer.data.get('scname', '')
                                        formatted_category = {
                                                  'cid': serializer.data['cid'],
                                                  'cname': serializer.data['cname'],
                                                  'scname': [subcategory.strip() for subcategory in scname.split(',')] if scname else []
                                        }
                                        formatted_data.append(formatted_category)

                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'Subcategory by name',
                                        'subcategories_byname': formatted_data
                              }
                              return Response(api_response)

                    except Artistcategories.DoesNotExist:
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_404_NOT_FOUND,
                                        'message': 'Category not found'
                              }
                              return Response(error_response)
                    except Exception as e:
                              error_message = 'An error occurred while fetching the category: {}'.format(str(e))
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
                                        'message': 'Categories details added successfully',
                                        'new_category': serializer.data,
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_message = 'Failed to add Category details:{}'.format(str(e))
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
                                        'updated_category': serializer.data,
                              }
                              return Response(api_response)

                    except Exception as e:
                              error_message = 'Failed to update product details: {}'.format(str(e))
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
                                        'message': 'Product partially updated successfully',
                                        'updated_category': serializer.data,
                              }
                              return Response(api_response)

                    except Exception as e:
                              error_message = 'Failed to partially update product details: {}'.format(str(e))
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
                                        'message': 'Categories deleted successfully',

                              }
                              return Response(api_response)
                    except Exception as e:
                              error_message = 'Failed to delete category details:{}'.format(str(e))
                              error_response = {'status': 'error',
                                                'code': status.HTTP_400_BAD_REQUEST,
                                                'message': error_message
                                                }
                    return Response(error_response)

