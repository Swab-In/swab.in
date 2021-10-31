from django.urls import path
from .views import *

urlpatterns = [
    # path('', HomeView.as_view, name='index'),
    path('/', HomeView.as_view() , name='index'),
    path('<int:pk>', ArticleDetail.as_view(), name='detailArtikel' )
]
