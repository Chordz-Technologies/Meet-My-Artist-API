from django.urls import path, include
from rest_framework import routers
from users.views import UserAPI, UserLoginAPI, ArtistByCategoryAPI, CarouselAPI, UserCountAPI, OrganiserByCategoryAPI
from .views import getWishlistAPI, addToWishlist, deleteFromWishlist
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
          path('userSearch/search/', UserAPI.as_view({'get':'search'})),
          path('userLogin/', UserLoginAPI.as_view()),

          path('artistbyCategory/<str:cname>/<str:scname>/', ArtistByCategoryAPI.as_view()),
          path('organiserbyCategory/<str:businesscategory>/', OrganiserByCategoryAPI.as_view()),
          path('imagesCarousel/', CarouselAPI.as_view()),
          path('userCount/', UserCountAPI.as_view()),

          path('getWishlist/<int:uid>/', getWishlistAPI.as_view()),
          path('addtoWishlist/<int:uid>/<int:wished_user_id>/', addToWishlist.as_view()),
          path('removefromWishlist/<int:uid>/<int:wished_user_id>/', deleteFromWishlist.as_view()),
]
