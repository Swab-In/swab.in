from django.urls import path
from .views import HomeView, ArticleDetail, json_req, add_comment, artikel_cards, get_comment

urlpatterns = [
    path('/', HomeView.as_view() , name='index'),
    path('<int:pk>', ArticleDetail.as_view(), name='detailArtikel'),
    path('/json_req', json_req , name='json_req'),
    path('/artikel_cards', artikel_cards , name='artikel_cards'),   
    path('/add_comment', add_comment , name='add_comment'),
    path('/get_comment', get_comment , name='get_comment'),

]