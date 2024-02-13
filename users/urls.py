from django.urls import path, include
from rest_framework import routers
from users.views import UserAPI, UserLoginAPI, ArtistByCategoryAPI, CarouselAPI, UserCountAPI

# router = routers.DefaultRouter()
# router.register(r'Users', UserAPI)


urlpatterns = [
          # path('api/', include(router.urls)),
          path('allUsers/', UserAPI.as_view({'get': 'list'})),
          path('userDetails/<int:pk>/', UserAPI.as_view({'get': 'retrieve'})),
          path('createUser/', UserAPI.as_view({'post': 'create'})),
          path('updateUser/<int:pk>/', UserAPI.as_view({'put': 'update'})),
          path('partialupdateUser/<int:pk>/', UserAPI.as_view({'patch': 'partial_update'})),
          path('deleteUser/<int:pk>/', UserAPI.as_view({'delete': 'destroy'})),

          path('artistsList/', UserAPI.as_view({'get': 'artistsList'})),
          path('organizersList/', UserAPI.as_view({'get': 'organizersList'})),
          path('usersList/', UserAPI.as_view({'get': 'usersList'})),

          path('userLogin/', UserLoginAPI.as_view()),

          path('artistbyCategory/<str:cname>/<str:scname>/', ArtistByCategoryAPI.as_view()),

          path('imagesCarousel/', CarouselAPI.as_view()),

          path('userCount/', UserCountAPI.as_view()),
]
