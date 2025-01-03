from django.urls import path
from . import views

app_name = 'jobs'  # Set the app namespace

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('search/', views.job_search, name='job_search'),
    path('<slug:slug>/', views.job_detail, name='job_detail'),  # Use slug here
]
