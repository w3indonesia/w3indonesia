from django.urls import path
from . import views

app_name = 'focuus'

urlpatterns = [
    path('', views.focuus_home, name='focuus_home'),
    path('category/<slug:category_slug>/', views.focuus_page, name='focuus_page'),
    path('category/<slug:category_slug>/stage/<slug:stage_slug>/', views.focuus_list, name='focuus_list'),
    path('article/<slug:article_slug>/', views.focuus_detail, name='focuus_detail_short'),
]
