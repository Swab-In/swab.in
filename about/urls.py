from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('contact', contactus, name='contactus'),
    path('json', json, name='json'),
    path('list-message', listcontact, name='listcontact')
]