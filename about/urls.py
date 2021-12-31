from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('contact', contactus, name='contactus'),
    path('json', func_json, name='json'),
    path('list-message', listcontact, name='listcontact'),
    path('pesan-post', pesan_post, name='pesan_post')
]