from django.urls import path
from artistcategories.views import ArtistcategoriesAPI

# router=routers.DefaultRouter()
# router.register('', categoriesAPI)

urlpatterns = [
          # path('', include(router.urls)),
          path('allCategories/', ArtistcategoriesAPI.as_view({'get': 'list'})),
          path('categoryDetails/<int:pk>/', ArtistcategoriesAPI.as_view({'get': 'retrieve'})),
          path('createCategory/', ArtistcategoriesAPI.as_view({'post': 'create'})),
          path('updateCategory/<int:pk>/', ArtistcategoriesAPI.as_view({'put': 'update'})),
          path('partialupdatecategory/<int:pk>/', ArtistcategoriesAPI.as_view({'patch': 'partial_update'})),
          path('deleteCategory/<int:pk>/', ArtistcategoriesAPI.as_view({'delete': 'destroy'})),
          path('subcategories/<str:cname>/', ArtistcategoriesAPI.as_view({'get': 'subcategories_byname'})),

]