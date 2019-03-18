from django.urls import path
from django.conf.urls import url, include
from auth0login.views import index, dashboard

urlpatterns = [
    path('', index),
    path('index', index),
    path('dashboard', dashboard),
    path('', include('django.contrib.auth.urls')),
    path('', include('social_django.urls')),
]