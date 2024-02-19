from django.urls import path
from businesscategories.views import BcategoryAPI

urlpatterns = [
          path('allBcategory/', BcategoryAPI.as_view({'get': 'list'})),
          path('bcategoryDetails/<int:pk>/', BcategoryAPI.as_view({'get': 'retrieve'})),
          path('createBcategory/', BcategoryAPI.as_view({'post': 'create'})),
          path('updateBcategory/<int:pk>/', BcategoryAPI.as_view({'put': 'update'})),
          path('partialupdateBcategory/<int:pk>/', BcategoryAPI.as_view({'patch': 'partial_update'})),
          path('deleteBcategory/<int:pk>/', BcategoryAPI.as_view({'delete': 'destroy'})),
]