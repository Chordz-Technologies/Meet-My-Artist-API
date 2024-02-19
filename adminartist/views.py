from adminartist.models import Adminartist
from adminartist.serializers import AdminSerializer, AdminLoginSerializer

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

class AdminAPI(ModelViewSet):
          queryset = Adminartist.objects.all()
          serializer_class = AdminSerializer

          def list(self, request, *args, **kwargs):
                    try:
                              admin = Adminartist.objects.all()
                              serializer = self.get_serializer(admin, many=True)
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'All admins',
                                        'all_admins': serializer.data,
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_msg = 'An error occurred while fetching records: {}'.format(str(e))
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
                                        'message': 'Admin details',
                                        'admin_details': serializer.data,
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_msg = 'An error occurred: {}'.format(str(e))
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                                        'message': error_msg,
                              }

          def create(self, request, *args, **kwargs):
                    try:
                              serializer = self.get_serializer(data=request.data)
                              serializer.is_valid(raise_exception=True)
                              serializer.save()
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_201_CREATED,
                                        'message': 'Admin added successfully',
                                        'new_admin': serializer.data,
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_msg = 'An error occurred: {}'.format(str(e))
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_400_BAD_REQUEST,
                                        'message': error_msg
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
                                        'updated_admin': 'Admin updated successfully',
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_msg = 'An error occurred: {}'.format(str(e))
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
                                        'updated_admin': 'Admin updated successfully',
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_msg = 'An error occurred: {}'.format(str(e))
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
                                        'message': 'Admin deleted successfully',
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_msg = 'An error occurred: {}'.format(str(e))
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_400_BAD_REQUEST,
                                        'message': error_msg,
                              }
                              return Response(error_response)

class AdminLoginAPI(APIView):
          serializer_class = AdminLoginSerializer

          def post(self, request, *args, **kwargs):
                    serializer = self.serializer_class(data=request.data)

                    if serializer.is_valid():
                              aname = serializer.validated_data.get('aname')
                              apassword = serializer.validated_data.get('apassword')

                              try:
                                        admin = Adminartist.objects.get(aname=aname)

                                        if admin.apssword == apassword:
                                                  return Response({'message': 'Valid User'}, status=status.HTTP_200_OK)
                                        else:
                                                  return Response({'message': 'Invalid Password'}, status=status.HTTP_401_UNAUTHORIZED)
                              except Adminartist.DoesNotExist:
                                        return Response({'message': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



