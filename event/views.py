import os
from datetime import datetime, timedelta
from django.db import transaction
from django.http import HttpResponse
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from event.models import Events
from event.serializers import EventSerializer, EventPosterSerializer

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
                              instance = serializer.save()

                              # Get the uploaded image instance
                              uploaded_image = instance.eposter

                              # Get the current file path
                              current_file_path = uploaded_image.path

                              # Specify the new file name
                              new_file_name = f'eposter_{instance.eid}.png'

                              # Create the new file path
                              new_file_path = os.path.join(os.path.dirname(current_file_path), new_file_name)

                              # Rename the file
                              os.rename(current_file_path, new_file_path)

                              # Update the instance with the new file name
                              instance.eposter.name = new_file_path

                              # Update the instance in the database with the new file name
                              instance.save()

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
                              with transaction.atomic():

                                        instance = self.get_object()
                                        serializer = self.get_serializer(instance, data=request.data)
                                        serializer.is_valid(raise_exception=True)
                                        instance = serializer.save()

                                        # Get the uploaded image instance
                                        uploaded_image = instance.eposter

                                        # Get the current file path
                                        current_file_path = uploaded_image.path

                                        # Specify the new file name
                                        new_file_name = f'eposter_{instance.eid}.png'

                                        # Create the new file path
                                        new_file_path = os.path.join(os.path.dirname(current_file_path), new_file_name)

                                        # Delete the old file if it exists
                                        if os.path.exists(new_file_path):
                                                  os.remove(new_file_path)

                                        # Rename the file
                                        os.rename(current_file_path, new_file_path)

                                        # Update the instance with the new file name
                                        instance.eposter.name = new_file_path

                                        # Update the instance in the database with the new file name
                                        instance.save()

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

class NotificationforEvents(APIView):
          def get(self, request):
                    try:
                              # Get current date
                              current_date = datetime.now().date()

                              # Calculate the date 3 days from now
                              three_days_later = current_date + timedelta(days=3)

                              # Query events happening within the next 3 days
                              upcoming_events = Events.objects.filter(edate__lte=three_days_later)

                              if upcoming_events.exists():
                                        # Serialize the data if needed
                                        serialized_data = []  # Assuming you have a serializer for the Events model
                                        for event in upcoming_events:
                                                  # Convert etime to a more user-friendly format
                                                  etime_formatted = event.etime.strftime(
                                                            "%I:%M%p") if event.etime else None
                                                  serialized_data.append({
                                                            'eid': event.eid,
                                                            'ename': event.ename,
                                                            'elocation': event.elocation,
                                                            'edate': event.edate,
                                                            'etime': etime_formatted,
                                                            'eposter': event.eposter,
                                                            'obuisnessname': event.obusinessname
                                                            # Add other fields as needed
                                                  })

                                        # Return success response
                                        return Response({
                                                  'status': 'success',
                                                  'code': status.HTTP_200_OK,
                                                  'message': 'Upcoming events found',
                                                  'data': serialized_data
                                        }, status=status.HTTP_200_OK)
                              else:
                                        # Return response for no events found
                                        return Response({
                                                  'status': 'success',
                                                  'code': status.HTTP_200_OK,
                                                  'message': 'No upcoming events found',
                                                  'data': []
                                        }, status=status.HTTP_200_OK)
                    except Exception as e:
                              # Return failure response
                              return Response({
                                        'status': 'error',
                                        'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                                        'message': 'Internal Server Error',
                                        'data': str(e)
                              }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetEventbyUid(generics.ListAPIView):
          serializer_class = EventSerializer

          def get(self, request, *args, **kwargs):
                    try:
                              user_id = self.kwargs.get('uid')
                              queryset = Events.objects.filter(uid=user_id)
                              serializer = self.get_serializer(instance=queryset,
                                                               many=True)  # Pass queryset as instance
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': f'All events by user {user_id}',
                                        'event_data': serializer.data,
                              }
                              return Response(api_response, status=status.HTTP_200_OK)  # Return 200 status
                    except Events.DoesNotExist:
                              api_response = {
                                        'status': 'error',
                                        'code': status.HTTP_404_NOT_FOUND,
                                        'message': f'No events found by user {user_id}',
                                        'event_data': [],
                              }
                              return Response(api_response, status=status.HTTP_404_NOT_FOUND)  # Return 404 status
                    except Exception as e:
                              error_msg = 'An error occurred: {}'.format(str(e))
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                                        'message': error_msg
                              }
                              return Response(error_response,
                                              status=status.HTTP_500_INTERNAL_SERVER_ERROR)  # Return 500 status

# class AddEventPoster(APIView):
#           serializer_class = EventPosterSerializer
#
#           def post(self, request, *args, **kwargs):
#                     serializer = self.serializer_class(data=request.data)
#
#                     if serializer.is_valid():
#                               event_id = serializer.validated_data.get('eventid')
#                               photo_base64 = serializer.validated_data.get('poster')
#
#                               # Specify the folder path for storing profile photos
#                               folder_name_event = 'event_posters'
#                               folder_path_event = os.path.join(settings.MEDIA_ROOT_EVENT, folder_name_event)
#                               os.makedirs(folder_path_event, exist_ok=True)
#
#                               photo_name = f'event_poster_{event_id}.png'  # Or any desired extension
#
#                               try:
#                                         # Write the base64 code to the file
#                                         with open(os.path.join(folder_path_event, photo_name), 'wb') as photo_file:
#                                                   photo_file.write(base64.b64decode(photo_base64))
#                               except Exception as e:
#                                         # Handle file writing errors
#                                         error_message = f'Error saving event poster: {str(e)}'
#                                         return Response({'error': error_message},
#                                                         status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#                               response_data = {
#                                         'status': 'success',
#                                         'code': status.HTTP_201_CREATED,
#                                         'message': 'Event poster uploaded successfully',
#                                         'photo_path': os.path.join(folder_path_event, photo_name)
#                               }
#                               return Response(response_data)
#
#                     return Response(serializer.errors)

class GetEventPoster(APIView):
          serializer_class = EventPosterSerializer

          def get(self, request, *args, **kwargs):
                    event_id = self.kwargs.get('eventid')

                    if not event_id:
                              return Response({'error': 'Event ID is required'}, status=status.HTTP_400_BAD_REQUEST)

                    try:
                              event_instance = Events.objects.get(eid=event_id)
                    except Events.DoesNotExist:
                              return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)

                    if not event_instance.eposter:
                              return Response({'error': 'Event poster not found'}, status=status.HTTP_404_NOT_FOUND)

                    image_path = event_instance.eposter.path

                    # Read the image file and return it as HttpResponse
                    with open(image_path, 'rb') as image_file:
                              return HttpResponse(image_file.read(),
                                                  content_type='image/png')  # Adjust content type as needed
