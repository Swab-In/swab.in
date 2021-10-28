from django.urls import path
from .views import index, informasi, add_pengalaman

urlpatterns = [
    path('', index, name='index'),
    path('informasi', informasi, name='informasi'),
    path('add-pengalaman', add_pengalaman, name='add_pengalaman'),
]
