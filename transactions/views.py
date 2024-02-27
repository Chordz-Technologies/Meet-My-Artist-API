from datetime import datetime, timedelta

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from transactions.models import Atransaction, Otransaction, Utransaction
from transactions.serializers import AtSerializer, OtSerializer, UtSerializer
from users.models import User

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

class SubscriptionforArtist(generics.ListAPIView):
          serializer_class = AtSerializer

          def get(self, request, *args, **kwargs):
                    try:
                              user_id = self.kwargs.get('uid')

                              if user_id is None:
                                        return Response({
                                                  'status': 'fail',
                                                  'code': status.HTTP_400_BAD_REQUEST,
                                                  'message': 'UserID not provided',
                                        })

                              current_date = datetime.now().date()

                              # Retrieve the latest transaction for the specified business_id
                              latest_transaction = Atransaction.objects.filter(uid=user_id).order_by('-atdate').first()

                              if not latest_transaction:
                                        return Response({
                                                  'status': 'success',
                                                  'code': status.HTTP_200_OK,
                                                  'message': f'No transactions found for UserID {user_id}',
                                        })

                              # Check if there is an associated subscription for the latest transaction
                              if latest_transaction.sid is None:
                                        return Response({
                                                  'status': 'success',
                                                  'code': status.HTTP_200_OK,
                                                  'message': f'No latest transaction found for UserID {user_id}',
                                        })

                              # Retrieve the subscription associated with the latest transaction
                              subscription = latest_transaction.sid

                              # Retrieve subscription duration
                              subscription_duration = subscription.sduration

                              # Calculate end date for the subscription
                              end_date = latest_transaction.atdate + timedelta(days=subscription_duration)

                              # Calculate remaining days for the subscription
                              remaining_days = max((end_date - current_date).days, 0)

                              if remaining_days <= 0:
                                        artist_status = 'Expired'
                              else:
                                        artist_status = 'Active'

                              # Update the artist status in the User table
                              user = User.objects.get(pk=user_id)
                              user.artiststatus = artist_status
                              user.save()

                              # Create the response dictionary with details from the latest transaction
                              response_data = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': f'Subscription details for UserID {user_id}',
                                        'data': [{
                                                  'end_date': end_date.strftime("%Y-%m-%d"),
                                                  'remaining_days': remaining_days,
                                                  'status': artist_status,
                                        }]
                              }
                              return Response(response_data)

                    except Exception as e:
                              # Handle other potential exceptions
                              return Response({
                                        'status': 'error',
                                        'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                                        'message': 'An error occurred',
                                        'data': str(e)
                              })

class SubscriptionforOrganizer(generics.ListAPIView):
          serializer_class = OtSerializer

          def get(self, request, *args, **kwargs):
                    try:
                              user_id = self.kwargs.get('uid')

                              if user_id is None:
                                        return Response({
                                                  'status': 'fail',
                                                  'code': status.HTTP_400_BAD_REQUEST,
                                                  'message': 'UserID not provided',
                                        })

                              current_date = datetime.now().date()

                              # Retrieve the latest transaction for the specified business_id
                              latest_transaction = Otransaction.objects.filter(uid=user_id).order_by('-otdate').first()

                              if not latest_transaction:
                                        return Response({
                                                  'status': 'success',
                                                  'code': status.HTTP_200_OK,
                                                  'message': f'No transactions found for UserID {user_id}',
                                        })

                              # Check if there is an associated subscription for the latest transaction
                              if latest_transaction.sid is None:
                                        return Response({
                                                  'status': 'success',
                                                  'code': status.HTTP_200_OK,
                                                  'message': f'No latest transaction found for UserID {user_id}',
                                        })

                              # Retrieve the subscription associated with the latest transaction
                              subscription = latest_transaction.sid

                              # Retrieve subscription duration
                              subscription_duration = subscription.sduration

                              # Calculate end date for the subscription
                              end_date = latest_transaction.otdate + timedelta(days=subscription_duration)

                              # Calculate remaining days for the subscription
                              remaining_days = max((end_date - current_date).days, 0)

                              if remaining_days <= 0:
                                        organizer_status = 'Expired'
                              else:
                                        organizer_status = 'Active'

                              # Update the artist status in the User table
                              user = User.objects.get(pk=user_id)
                              user.organizerstatus = organizer_status
                              user.save()

                              # Create the response dictionary with details from the latest transaction
                              response_data = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': f'Subscription details for UserID {user_id}',
                                        'data': [{
                                                  'end_date': end_date.strftime("%Y-%m-%d"),
                                                  'remaining_days': remaining_days,
                                                  'status': organizer_status,
                                        }]
                              }
                              return Response(response_data)

                    except Exception as e:
                              # Handle other potential exceptions
                              return Response({
                                        'status': 'error',
                                        'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                                        'message': 'An error occurred',
                                        'data': str(e)
                              })

class SubscriptionforUser(generics.ListAPIView):
          serializer_class = UtSerializer

          def get(self, request, *args, **kwargs):
                    try:
                              user_id = self.kwargs.get('uid')

                              if user_id is None:
                                        return Response({
                                                  'status': 'fail',
                                                  'code': status.HTTP_400_BAD_REQUEST,
                                                  'message': 'UserID not provided',
                                        })

                              current_date = datetime.now().date()

                              # Retrieve the latest transaction for the specified business_id
                              latest_transaction = Utransaction.objects.filter(uid=user_id).order_by('-utdate').first()

                              if not latest_transaction:
                                        return Response({
                                                  'status': 'success',
                                                  'code': status.HTTP_200_OK,
                                                  'message': f'No transactions found for UserID {user_id}',
                                        })

                              # Check if there is an associated subscription for the latest transaction
                              if latest_transaction.sid is None:
                                        return Response({
                                                  'status': 'success',
                                                  'code': status.HTTP_200_OK,
                                                  'message': f'No latest transaction found for UserID {user_id}',
                                        })

                              # Retrieve the subscription associated with the latest transaction
                              subscription = latest_transaction.sid

                              # Retrieve subscription duration
                              subscription_duration = subscription.sduration

                              # Calculate end date for the subscription
                              end_date = latest_transaction.otdate + timedelta(days=subscription_duration)

                              # Calculate remaining days for the subscription
                              remaining_days = max((end_date - current_date).days, 0)

                              if remaining_days <= 0:
                                        user_status = 'Expired'
                              else:
                                        user_status = 'Active'

                              # Update the artist status in the User table
                              user = User.objects.get(pk=user_id)
                              user.userstatus = user_status
                              user.save()

                              # Create the response dictionary with details from the latest transaction
                              response_data = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': f'Subscription details for UserID {user_id}',
                                        'data': [{
                                                  'end_date': end_date.strftime("%Y-%m-%d"),
                                                  'remaining_days': remaining_days,
                                                  'status': user_status,
                                        }]
                              }
                              return Response(response_data)

                    except Exception as e:
                              # Handle other potential exceptions
                              return Response({
                                        'status': 'error',
                                        'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                                        'message': 'An error occurred',
                                        'data': str(e)
                              })

class ASubscriptionEndingSoon(generics.ListAPIView):
          serializer_class = AtSerializer

          def get(self, request):
                    try:
                              # Get current date
                              current_date = datetime.now().date()

                              # Retrieve transactions
                              transactions = Atransaction.objects.all()

                              # Collect subscriptions ending soon
                              ending_soon = []
                              for transaction in transactions:
                                        # Access the related Subscription object via the ForeignKey relationship
                                        subscription = transaction.sid

                                        if subscription is not None:
                                                  # Get the duration from the subscription object
                                                  duration = subscription.sduration

                                                  # Calculate the end date based on subscription start date and duration
                                                  end_date = transaction.atdate + timedelta(days=duration)

                                                  # Calculate remaining days until the subscription ends
                                                  remaining_days = (end_date - current_date).days

                                                  # Check if remaining days are within the range of 1 to 7
                                                  if 1 <= remaining_days <= 7:
                                                            # Access the related User object via the ForeignKey relationship
                                                            user = transaction.uid

                                                            ending_soon.append({
                                                                      'user_id': user.uid,
                                                                      'user_name': user.uname,
                                                                      'contact_no': user.uwhatsappno,
                                                                      'user_email': user.uemail,
                                                                      'subscription_date': transaction.atdate,
                                                                      'remaining_days': remaining_days,
                                                                      # Add more fields as required
                                                            })

                              if ending_soon:
                                        return Response({
                                                  'status': 'success',
                                                  'code': 200,
                                                  'message': 'Artist subscriptions ending soon',
                                                  'data': ending_soon
                                        })
                              else:
                                        return Response({
                                                  'status': 'fail',
                                                  'code': 404,
                                                  'message': 'No artist subscriptions expiring soon',
                                                  'data': []
                                        })

                    except Exception as e:
                              # Handle other potential exceptions
                              return Response({
                                        'status': 'error',
                                        'code': 500,
                                        'message': 'An error occurred',
                                        'data': str(e)
                              })

class OSubscriptionEndingSoon(generics.ListAPIView):
          serializer_class = OtSerializer

          def get(self, request):
                    try:
                              # Get current date
                              current_date = datetime.now().date()

                              # Retrieve transactions
                              transactions = Otransaction.objects.all()

                              # Collect subscriptions ending soon
                              ending_soon = []
                              for transaction in transactions:
                                        # Access the related Subscription object via the ForeignKey relationship
                                        subscription = transaction.sid

                                        if subscription is not None:
                                                  # Get the duration from the subscription object
                                                  duration = subscription.sduration

                                                  # Calculate the end date based on subscription start date and duration
                                                  end_date = transaction.otdate + timedelta(days=duration)

                                                  # Calculate remaining days until the subscription ends
                                                  remaining_days = (end_date - current_date).days

                                                  # Check if remaining days are within the range of 1 to 7
                                                  if 1 <= remaining_days <= 7:
                                                            # Access the related User object via the ForeignKey relationship
                                                            user = transaction.uid

                                                            ending_soon.append({
                                                                      'user_id': user.uid,
                                                                      'user_name': user.uname,
                                                                      'contact_no': user.uwhatsappno,
                                                                      'user_email': user.uemail,
                                                                      'subscription_date': transaction.otdate,
                                                                      'remaining_days': remaining_days,
                                                                      # Add more fields as required
                                                            })

                              if ending_soon:
                                        return Response({
                                                  'status': 'success',
                                                  'code': 200,
                                                  'message': 'Organizer subscriptions ending soon',
                                                  'data': ending_soon
                                        })
                              else:
                                        return Response({
                                                  'status': 'fail',
                                                  'code': 404,
                                                  'message': 'No organizer subscriptions expiring soon',
                                                  'data': []
                                        })

                    except Exception as e:
                              # Handle other potential exceptions
                              return Response({
                                        'status': 'error',
                                        'code': 500,
                                        'message': 'An error occurred',
                                        'data': str(e)
                              })

class USubscriptionEndingSoon(generics.ListAPIView):
          serializer_class = UtSerializer

          def get(self, request):
                    try:
                              # Get current date
                              current_date = datetime.now().date()

                              # Retrieve transactions
                              transactions = Utransaction.objects.all()

                              # Collect subscriptions ending soon
                              ending_soon = []
                              for transaction in transactions:
                                        # Access the related Subscription object via the ForeignKey relationship
                                        subscription = transaction.sid

                                        if subscription is not None:
                                                  # Get the duration from the subscription object
                                                  duration = subscription.sduration

                                                  # Calculate the end date based on subscription start date and duration
                                                  end_date = transaction.utdate + timedelta(days=duration)

                                                  # Calculate remaining days until the subscription ends
                                                  remaining_days = (end_date - current_date).days

                                                  # Check if remaining days are within the range of 1 to 7
                                                  if 1 <= remaining_days <= 7:
                                                            # Access the related User object via the ForeignKey relationship
                                                            user = transaction.uid

                                                            ending_soon.append({
                                                                      'user_id': user.uid,
                                                                      'user_name': user.uname,
                                                                      'contact_no': user.uwhatsappno,
                                                                      'user_email': user.uemail,
                                                                      'subscription_date': transaction.utdate,
                                                                      'remaining_days': remaining_days,
                                                                      # Add more fields as required
                                                            })

                              if ending_soon:
                                        return Response({
                                                  'status': 'success',
                                                  'code': 200,
                                                  'message': 'User subscriptions ending soon',
                                                  'data': ending_soon
                                        })
                              else:
                                        return Response({
                                                  'status': 'fail',
                                                  'code': 404,
                                                  'message': 'No user subscriptions expiring soon',
                                                  'data': []
                                        })

                    except Exception as e:
                              # Handle other potential exceptions
                              return Response({
                                        'status': 'error',
                                        'code': 500,
                                        'message': 'An error occurred',
                                        'data': str(e)
                              })
