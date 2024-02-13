from django.urls import path
from transactions.views import AtransactionAPI, OtransactionAPI, UtransactionAPI

urlpatterns = [
          path('allAtransactions/', AtransactionAPI.as_view({'get': 'list'})),
          path('atransactionDetails/<int:pk>/', AtransactionAPI.as_view({'get': 'retrieve'})),
          path('createAtransaction/', AtransactionAPI.as_view({'post': 'create'})),
          path('updateAtransaction/<int:pk>/', AtransactionAPI.as_view({'put': 'update'})),
          path('partialupdateAtransaction/<int:pk>/', AtransactionAPI.as_view({'patch': 'partial_update'})),
          path('deleteAtransaction/<int:pk>/', AtransactionAPI.as_view({'delete': 'destroy'})),

          path('allOtransactions/', OtransactionAPI.as_view({'get': 'list'})),
          path('otransactionDetails/<int:pk>/', OtransactionAPI.as_view({'get': 'retrieve'})),
          path('createOtransaction/', OtransactionAPI.as_view({'post': 'create'})),
          path('updateOtransaction/<int:pk>/', OtransactionAPI.as_view({'put': 'update'})),
          path('partialupdateOtransaction/<int:pk>/', OtransactionAPI.as_view({'patch': 'partial_update'})),
          path('deleteOtransaction/<int:pk>/', OtransactionAPI.as_view({'delete': 'destroy'})),

          path('allUtransactions/', UtransactionAPI.as_view({'get': 'list'})),
          path('utransactionDetails/<int:pk>/', UtransactionAPI.as_view({'get': 'retrieve'})),
          path('createUtransaction/', UtransactionAPI.as_view({'post': 'create'})),
          path('updateUtransaction/<int:pk>/', UtransactionAPI.as_view({'put': 'update'})),
          path('partialupdateUtransaction/<int:pk>/', UtransactionAPI.as_view({'patch': 'partial_update'})),
          path('deleteUtransaction/<int:pk>/', UtransactionAPI.as_view({'delete': 'destroy'})),
]