from django.urls import path
from artistcategories.views import ArtistcategoriesAPI

# router=routers.DefaultRouter()
# router.register('', categoriesAPI)

urlpatterns = [
          # path('', include(router.urls)),
          path('allAcategories/', ArtistcategoriesAPI.as_view({'get': 'list'})),
          path('acategoryDetails/<int:pk>/', ArtistcategoriesAPI.as_view({'get': 'retrieve'})),
          path('createAcategory/', ArtistcategoriesAPI.as_view({'post': 'create'})),
          path('updateAcategory/<int:pk>/', ArtistcategoriesAPI.as_view({'put': 'update'})),
          path('partialupdateAcategory/<int:pk>/', ArtistcategoriesAPI.as_view({'patch': 'partial_update'})),
          path('deleteAcategory/<int:pk>/', ArtistcategoriesAPI.as_view({'delete': 'destroy'})),
          path('subcategories/<str:cname>/', ArtistcategoriesAPI.as_view({'get': 'subcategories_byname'})),

]