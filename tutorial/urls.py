from django.urls import path
from . import views

app_name = 'tutorial'

urlpatterns = [
    path('', views.homepage, name='home'),
    path('<slug:category_slug>/', views.tutorial_page, name='tutorial_page'),
    path('<slug:category_slug>/<slug:subcategory_slug>/', views.article_list, name='article_list'),
    path('<slug:category_slug>/<slug:subcategory_slug>/<slug:article_slug>/', views.article_detail, name='article_detail'),
]
