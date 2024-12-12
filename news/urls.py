from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('page/<int:page_number>/', views.news_page, name='news_page'),
    path('', views.news_list, name='news_list'),
    path('<slug:category_slug>/', views.news_by_category, name='news_by_category'),
    path('<str:category_slug>/<str:news_slug>/', views.news_detail, name='news_detail'),
]
