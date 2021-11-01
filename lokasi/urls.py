from django.urls import path, include
from . import views
from .views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='lokasi'),
    path('<int:pk>/forum', PostDetailView.as_view(), name='post-detail'),
    path('new/', PostCreateView.as_view(), name='post-create'),
]