from django.urls import path
from .views import *
from lokasi.views import *

app_name = "forum"

urlpatterns = [
    path('', index, name='index'),
    path('list', List_forumView.as_view(), name="list"),
    path('detail/<int:pk>', ForumDetail.as_view(), name='forum-detail'),
    path('json_req', json_req, name="json_req"),
    # path('json_forum', json_forum, name="json_forum"),
    # path('add_forum', add_forum, name='add_forum'),
    # path('json_lokasi', json_lokasi, name='json_lokasi'),
    path('forum_content', forum_content, name="forum_content"),
    path('komentar_post', komentar_post, name="post_komentar"),
    path('get_komentar', all_komentar, name="all_komentar"),
    path('json_forum', json_forum, name="json_forum"),
    path('add_forum', add_forum, name='add_forum'),
    path('json_lokasi', json_lokasi, name='json_lokasi'),
]
