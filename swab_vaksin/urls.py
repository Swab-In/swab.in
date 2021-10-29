from django.urls import path
from .views import index, informasi

urlpatterns = [
    path('', index, name='index'),
    path('informasi', informasi, name='informasi'),
]
