from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', views.login, name='login'),
    path('custom_login/', views.custom_login, name='custom_login'),
]
