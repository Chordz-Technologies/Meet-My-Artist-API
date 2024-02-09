from event.models import Events
from event.serializers import EventSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class EventAPI(ModelViewSet):
          queryset = Events.objects.all()
          serializer_class = EventSerializer

          def list(self, request, *args, **kwargs):
                    try:
                              event = Events.objects.all()
                              serializer = self.get_serializer(event, many=True)
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'ALL Events',
                                        'all_events': serializer.data,
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_message = 'An error occurred while fetching Events details: {}'.format(str(e))
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
                                        'message': 'Events details fetched successfully',
                                        'events_details': serializer.data,
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_message = 'An error occurred while fetching events: {}'.format(str(e))
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
                                        'message': 'Events details added successfully',
                                        'new_event': serializer.data,
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_message = 'Failed to add event details:{}'.format(str(e))
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
                                        'message': 'Event updated successfully',
                                        'updated_event': serializer.data,
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_message = 'Failed to update Event details:{}'.format(str(e))
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
                                        'message': 'Event updated successfully',
                                        'updated_event': serializer.data,
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_message = 'Failed to partially update event details:{}'.format(str(e))
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
                                        'message': 'Event deleted successfully',
                              }
                              return Response(api_response, status=status.HTTP_200_OK)
                    except Exception as e:
                              error_message = 'Failed to delete Event details:{}'.format(str(e))
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_400_BAD_REQUEST,
                                        'message': error_message
                                        }
                    return Response(error_response)
