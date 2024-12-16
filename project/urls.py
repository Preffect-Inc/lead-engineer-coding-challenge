from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('users/', include('app.urls')),  # Routes user-related functionality
]