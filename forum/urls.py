from django.urls import path
from .views import *
from lokasi.views import *

app_name = "forum"

urlpatterns = [
    path('', index, name='index'),
    path('list', List_forumView.as_view(), name="list"),
    path('detail/<int:pk>', ForumDetail.as_view(), name='forum-detail'),
    path('json', json, name="json-req")
]
