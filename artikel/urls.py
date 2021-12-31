from django.urls import path
from .views import HomeView, ArticleDetail, artikel_content, json_req

urlpatterns = [
    path('/', HomeView.as_view() , name='index'),
    path('<int:pk>', ArticleDetail.as_view(), name='detailArtikel'),
    path('/json_req', json_req , name='json_req'),
    path('/artikel_content', artikel_content , name='artikel_content'),
]