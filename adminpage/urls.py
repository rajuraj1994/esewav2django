from django.urls import path 
from .views import admin_home


urlpatterns=[
    path('dashboard/',admin_home)
]