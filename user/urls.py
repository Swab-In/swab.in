from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/', authenticate_login, name='login'),
    # path('auth/', authenticate_login, name='auth'),
    path('logout/', Userlogout, name='logout'),
    path('register/', UserRegister, name='register'),
]
