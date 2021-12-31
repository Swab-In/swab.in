from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('list-informasi', ListView.as_view(), name='list_informasi'),
    path('informasi-swab/<int:pk>', InfoDetailSwab.as_view(), name='informasi-swab'),
    path('informasi-vaksin/<int:pk>', InfoDetailVaksin.as_view(), name='informasi-vaksin'),
    path('json-swab', jsonSwab, name='json-swab'),
    path('json-vaksin', jsonVaksin, name='json-vaksin'),
    path('json-info-vaksin', jsonInfoVaksin, name='json-info-vaksin'),
    path('json-info-swab', jsonInfoSwab, name='json-info-swab'),
    path('add-experience', addExperience, name='add-experience'),
]
