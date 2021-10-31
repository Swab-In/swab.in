from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    # path('lokasi', LokasiList.as_view(), name='index'),
    # path('forum/<int:pk>', LokasiDetail.as_view(), name='lokasi-detail')
]
