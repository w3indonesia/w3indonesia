"""
URL configuration for Merdeka project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tutorial/', include('tutorial.urls')),
    path('bootcamp/', include('bootcamp.urls')),
    path('jobs/', include('jobs.urls')),
    path('news/', include('news.urls')),
    path('scholarship/', include('scholarship.urls')),
    path('contact/', include('contact.urls')),
    path('', include('home.urls')),
] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = 'tutorial.views.custom_bad_request_view'
handler401 = 'tutorial.views.error_401'
handler403 = 'tutorial.views.custom_permission_denied_view'
handler404 = 'tutorial.views.custom_page_not_found_view'
handler405 = 'tutorial.views.error_405'
handler429 = 'tutorial.views.error_429'
handler500 = 'tutorial.views.custom_error_view'
handler502 = 'tutorial.views.error_502'
handler503 = 'tutorial.views.error_503'
