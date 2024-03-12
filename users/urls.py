from django.urls import path

from users.views import UserAPI, UserLoginAPI, ArtistByCategoryAPI, UserCountAPI, OrganizerByCategoryAPI, \
          getWishlistAPI, addToWishlist, deleteFromWishlist, getLikesAPI, addToLikes, deleteFromLikes, \
          GetProfilePhoto, AddMultiplePhotos, GetMultiplePhotos, GetCarouselImages, AddCarouselImages, SendMessageAPI

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
          path('userSearch/', UserAPI.as_view({'get': 'search'})),
          path('userLogin/', UserLoginAPI.as_view()),
          path('userCount/', UserCountAPI.as_view()),

          path('artistbyCategory/<str:cname>/<str:scname>/', ArtistByCategoryAPI.as_view()),
          path('organizerbyCategory/<str:businesscategory>/', OrganizerByCategoryAPI.as_view()),

          path('getCarouselImages/', GetCarouselImages.as_view()),
          path('addCarouselImages/', AddCarouselImages.as_view()),

          path('getProfilePhoto/<int:uid>/', GetProfilePhoto.as_view()),
          # path('addProfilePhoto/', AddProfilePhoto.as_view()),

          path('getMultiplePhotos/<int:userid>/', GetMultiplePhotos.as_view()),
          path('addMultiplePhotos/', AddMultiplePhotos.as_view()),

          path('getWishlist/<int:uid>/', getWishlistAPI.as_view()),
          path('addtoWishlist/<int:uid>/<int:wished_user_id>/', addToWishlist.as_view()),
          path('removefromWishlist/<int:uid>/<int:wished_user_id>/', deleteFromWishlist.as_view()),

          path('getTotalLikes/<int:uid>/', getLikesAPI.as_view()),
          path('addtoLikes/<int:uid>/<int:liked_user_id>/', addToLikes.as_view()),
          path('removefromLikes/<int:uid>/<int:liked_user_id>/', deleteFromLikes.as_view()),

          path('sendMessage/', SendMessageAPI.as_view()),

]
