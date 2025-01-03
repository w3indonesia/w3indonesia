from django.urls import path
from . import views

app_name = 'scholarships'

urlpatterns = [
    path('', views.scholarship_list, name='scholarship_list'),
    path('search/', views.scholarship_search, name='scholarship_search'),
    path('<slug:slug>/', views.scholarship_detail, name='scholarship_detail'),
]
