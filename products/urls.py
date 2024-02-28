from django.urls import path
from products.views import ProductsAPI, AddProductPhoto, GetProductPhoto

# router = routers.DefaultRouter()
# router.register('', views.productsAPI)

urlpatterns = [
          # path('api/', include(router.urls)),
          path('allProducts/', ProductsAPI.as_view({'get': 'list'})),
          path('productDetails/<int:pk>/', ProductsAPI.as_view({'get': 'retrieve'})),
          path('createProduct/', ProductsAPI.as_view({'post': 'create'})),
          path('updateProduct/<int:pk>/', ProductsAPI.as_view({'put': 'update'})),
          path('partialupdateProduct/<int:pk>/', ProductsAPI.as_view({'patch': 'partial_update'})),
          path('deleteProduct/<int:pk>/', ProductsAPI.as_view({'delete': 'destroy'})),

          path('addProductPhoto/', AddProductPhoto.as_view()),
          path('getProductPhoto/<int:productid>/', GetProductPhoto.as_view()),
]
