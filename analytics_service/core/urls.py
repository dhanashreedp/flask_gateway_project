from django.urls import path
from .views import track_event

urlpatterns = [
    path('track/', track_event),
]
