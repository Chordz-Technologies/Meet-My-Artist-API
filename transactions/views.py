from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from transactions.models import Atransaction, Otransaction, Utransaction
from transactions.serializers import AtSerializer, OtSerializer, UtSerializer

# Create your views here.

class AtransactionAPI(ModelViewSet):
          queryset = Atransaction.objects.all()
          serializer_class = AtSerializer

          def list(self, request, *args, **kwargs):
                    try:
                              atransaction = Atransaction.objects.all()
                              serializer = self.get_serializer(atransaction, many=True)
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'All artists transactions',
                                        'all_atransactions': serializer.data,
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
                              serializer = self.get_serializer(instance)
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'Atransaction by ID',
                                        'atransaction_details': serializer.data,
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
                              serializer = self.get_serializer(data=request.data)
                              serializer.is_valid(raise_exception=True)
                              serializer.save()
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_201_CREATED,
                                        'message': 'Atransaction created successfully',
                                        'new_atransaction': serializer.data,
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
                              serializer.save()
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'Atransaction updated successfully',
                                        'updated_atransaction': serializer.data,
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
                              serializer = self.get_serializer(instance, data=request.data, partial=True)
                              serializer.is_valid(raise_exception=True)
                              serializer.save()
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'Atransaction partially updated successfully',
                                        'updated_atransaction': serializer.data,
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
                                        'message': 'Atransaction deleted successfully',
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

class OtransactionAPI(ModelViewSet):
          queryset = Otransaction.objects.all()
          serializer_class = OtSerializer

          def list(self, request, *args, **kwargs):
                    try:
                              atransaction = Otransaction.objects.all()
                              serializer = self.get_serializer(atransaction, many=True)
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'All organizers transactions',
                                        'all_otransactions': serializer.data,
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
                              serializer = self.get_serializer(instance)
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'Otransaction by ID',
                                        'otransaction_details': serializer.data,
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
                              serializer = self.get_serializer(data=request.data)
                              serializer.is_valid(raise_exception=True)
                              serializer.save()
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_201_CREATED,
                                        'message': 'Otransaction created successfully',
                                        'new_otransaction': serializer.data,
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
                              serializer.save()
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'Otransaction updated successfully',
                                        'updated_otransaction': serializer.data,
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
                              serializer = self.get_serializer(instance, data=request.data, partial=True)
                              serializer.is_valid(raise_exception=True)
                              serializer.save()
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'Otransaction partially updated successfully',
                                        'updated_otransaction': serializer.data,
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
                                        'message': 'Otransaction deleted successfully',
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

class UtransactionAPI(ModelViewSet):
          queryset = Utransaction.objects.all()
          serializer_class = UtSerializer

          def list(self, request, *args, **kwargs):
                    try:
                              atransaction = Utransaction.objects.all()
                              serializer = self.get_serializer(atransaction, many=True)
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'All users transactions',
                                        'all_utransactions': serializer.data,
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
                              serializer = self.get_serializer(instance)
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'Utransaction by ID',
                                        'utransaction_details': serializer.data,
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
                              serializer = self.get_serializer(data=request.data)
                              serializer.is_valid(raise_exception=True)
                              serializer.save()
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_201_CREATED,
                                        'message': 'Utransaction created successfully',
                                        'new_utransaction': serializer.data,
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
                              serializer.save()
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'Utransaction updated successfully',
                                        'updated_utransaction': serializer.data,
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
                              serializer = self.get_serializer(instance, data=request.data, partial=True)
                              serializer.is_valid(raise_exception=True)
                              serializer.save()
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'Utransaction partially updated successfully',
                                        'updated_utransaction': serializer.data,
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
                                        'message': 'Utransaction deleted successfully',
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