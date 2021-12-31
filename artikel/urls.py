from django.urls import path
from .views import HomeView, ArticleDetail, json

urlpatterns = [
    path('/', HomeView.as_view() , name='index'),
    path('<int:pk>', ArticleDetail.as_view(), name='detailArtikel'),
    path('/json', json , name='json'),
]