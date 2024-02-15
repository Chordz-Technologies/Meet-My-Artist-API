from django.utils.datastructures import MultiValueDict
from subscription.models import Subscription
from subscription.serializers import SubscriptionSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class SubscriptionAPI(ModelViewSet):
          queryset = Subscription.objects.all()
          serializer_class = SubscriptionSerializer

          def list(self, request, *args, **kwargs):
                    try:
                              subscription = Subscription.objects.all()
                              serializer = self.get_serializer(subscription, many=True)
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'ALL Subscriptions',
                                        'all_subscription': serializer.data,
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_message = 'An error occurred while fetching Subscription details: {}'.format(str(e))
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                                        'message': error_message
                              }
                    return Response(error_response)

          def user_subscriptions(self, request, *args, **kwargs):
                    try:
                              subscriptions = Subscription.objects.filter(planfor__iexact='User')
                              serializer = self.get_serializer(subscriptions, many=True)

                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'All users subscriptions',
                                        'user_subscriptions': serializer.data,
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_msg = 'user subscription error: {}'.format(str(e))
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                                        'message': error_msg,
                              }
                              return Response(error_response)

          def organizer_subscriptions(self, request, *args, **kwargs):
                    try:
                              subscription = Subscription.objects.filter(planfor__iexact='Organizer')
                              serializer = self.get_serializer(subscription, many=True)

                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'All organizers subscriptions',
                                        'organizer_subscriptions': serializer.data,
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

          def artist_subscriptions(self, request, *args, **kwargs):
                    try:
                              subscriptions = Subscription.objects.filter(planfor__iexact='Artist')
                              serializer = self.get_serializer(subscriptions, many=True)

                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'all artists subscriptions',
                                        'artist_subscriptions': serializer.data
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

          def retrieve(self, request, *args, **kwargs):
                    try:
                              instance = self.get_object()
                              serializer = self.get_serializer(instance)
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'Subscription details fetched successfully',
                                        'subscription_details': serializer.data,
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_message = 'An error occurred while fetching subscription: {}'.format(str(e))
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
                                        'message': 'New subscription added successfully',
                                        'new_subscription': serializer.data,
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_message = 'Failed to add subscription :{}'.format(str(e))
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
                                        'message': 'Subscription updated successfully',
                                        'updated_subscription': serializer.data,
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_message = 'Failed to update Subscription :{}'.format(str(e))
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
                                        'message': 'Subscription partially updated successfully',
                                        'updated_subscription': serializer.data,
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_message = 'Failed to partially update subscription :{}'.format(str(e))
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
                                        'message': 'Subscription deleted successfully',

                              }
                              return Response(api_response)
                    except Exception as e:
                              error_message = 'Failed to delete Subscription :{}'.format(str(e))
                              error_response = {'status': 'error',
                                                'code': status.HTTP_400_BAD_REQUEST,
                                                'message': error_message
                                                }
                              return Response(error_response)
