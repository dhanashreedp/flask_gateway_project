from django.urls import path
from .views import register, login

urlpatterns = [
    path('register/', register),  # /api/register/
    path('login/', login),        # /api/login/
]
