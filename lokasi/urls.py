from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, json

urlpatterns = [
    path('', PostListView.as_view(), name='lokasi'),
    path('forum/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('new/', PostCreateView.as_view(), name='post-create'),
    path('json/', json, name="json")
]