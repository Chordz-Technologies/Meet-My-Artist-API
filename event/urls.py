from django.urls import path
from event.views import EventAPI, NotificationforEvents, GetEventbyUid, GetEventPoster

# router = routers.DefaultRouter()
# router.register('', eventAPI)

urlpatterns = [
          # path('', include(router.urls)),
          path('allEvents/', EventAPI.as_view({'get': 'list'})),
          path('eventDetails/<int:pk>/', EventAPI.as_view({'get': 'retrieve'})),
          path('createEvent/', EventAPI.as_view({'post': 'create'})),
          path('updateEvent/<int:pk>', EventAPI.as_view({'put': 'update'})),
          path('partialupdateEvent/<int:pk>/', EventAPI.as_view({'patch': 'partial_update'})),
          path('deleteEvent/<int:pk>/', EventAPI.as_view({'delete': 'destroy'})),

          path('eventNotifications/', NotificationforEvents.as_view()),

          path('getEventsbyUid/<int:uid>/', GetEventbyUid.as_view()),

          path('getEventPoster/<int:eventid>/', GetEventPoster.as_view()),
          # path('addEventPoster/', AddEventPoster.as_view()),

]
