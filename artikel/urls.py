from django.urls import path
from .views import *

urlpatterns = [
    # path('', HomeView.as_view, name='index'),
    path('artikel/', HomeView.as_view() , name='index'),
    path('artikel/<int:pk>', ArticleDetail.as_view(), name='detailArtikel' )
]
