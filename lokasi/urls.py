from django.urls import path, include
from . import views
from .views import *

app_name = "lokasi"

urlpatterns = [
    path('', PostListView.as_view(), name='lokasi'),
    path('forum/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('new/', PostCreateView.as_view(), name='post-create'),
    path('json', json, name='json'),
    path('add_post', add_post, name='add_post'),
]