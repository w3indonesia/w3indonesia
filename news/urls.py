from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('load-more-news/', views.load_more_news, name='load_more_news'),
    path('', views.news_list, name='news_list'),
    path('<slug:category_slug>/', views.category_articles, name='news_by_category'),  
    path('<slug:slug>/', views.category_articles, name='category_articles'),
    path('<slug:category_slug>/<slug:news_slug>/', views.news_detail, name='news_detail'),
]
