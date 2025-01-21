import razorpay
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from subscription.models import Subscription, Payment
from subscription.serializers import SubscriptionSerializer
from users.models import User

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

class CreateRazorpayOrder(APIView):
          def post(self, request, subscription_id):
                    try:
                              # Fetch the subscription
                              subscription = Subscription.objects.get(sid=subscription_id)
                              amount = int(float(subscription.sprice) * 100)  # Convert to paise

                              # Create Razorpay client
                              client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))

                              # Create Razorpay order
                              order_data = {
                                        'amount': amount,
                                        'currency': 'INR',
                                        'payment_capture': 1
                              }
                              order = client.order.create(data=order_data)

                              # Create and save the payment record
                              payment = Payment.objects.create(
                                        subscription=subscription,
                                        razorpay_order_id=order['id'],
                                        amount=amount / 100,  # Convert back to INR
                                        currency='INR',
                                        payment_status='pending'
                              )

                              return Response({
                                        'status': 'success',
                                        'order_id': order['id'],
                                        'amount': amount,
                                        'currency': 'INR',
                                        'subscription': SubscriptionSerializer(subscription).data,
                                        'payment': {
                                                  'payment_id': payment.id,
                                                  'razorpay_order_id': payment.razorpay_order_id,
                                                  'status': payment.payment_status
                                        }
                              }, status=status.HTTP_201_CREATED)

                    except Subscription.DoesNotExist:
                              return Response({'error': 'Subscription not found'}, status=status.HTTP_404_NOT_FOUND)
                    except Exception as e:
                              return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class VerifyRazorpayPayment(APIView):
          def post(self, request):
                    try:
                              # Extract data from the request
                              razorpay_payment_id = request.data.get('razorpay_payment_id')
                              razorpay_order_id = request.data.get('razorpay_order_id')
                              razorpay_signature = request.data.get('razorpay_signature')

                              # Ensure all required fields are present
                              if not all([razorpay_payment_id, razorpay_order_id, razorpay_signature]):
                                        return Response({'status': 'error', 'message': 'Missing required fields'},
                                                        status=status.HTTP_400_BAD_REQUEST)

                              # Fetch the payment object using razorpay_order_id
                              payment = Payment.objects.get(razorpay_order_id=razorpay_order_id)

                              # Verify the signature
                              client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))
                              params_dict = {
                                        'razorpay_order_id': razorpay_order_id,
                                        'razorpay_payment_id': razorpay_payment_id,
                                        'razorpay_signature': razorpay_signature
                              }

                              # Verify the payment signature
                              client.utility.verify_payment_signature(params_dict)

                              # Update the payment status to 'completed'
                              payment.payment_status = 'completed'
                              payment.save()

                              return Response({
                                        'status': 'success',
                                        'message': 'Payment verified successfully',
                                        'payment_id': payment.id
                              }, status=status.HTTP_200_OK)

                    except razorpay.errors.SignatureVerificationError:
                              return Response({'status': 'error', 'message': 'Payment verification failed'},
                                              status=status.HTTP_400_BAD_REQUEST)
                    except Payment.DoesNotExist:
                              return Response({'status': 'error', 'message': 'Payment record not found'},
                                              status=status.HTTP_404_NOT_FOUND)
                    except Exception as e:
                              return Response({'status': 'error', 'message': str(e)},
                                              status=status.HTTP_500_INTERNAL_SERVER_ERROR)
