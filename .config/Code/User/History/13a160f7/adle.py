from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('all/', views.getEvent),
    path('post/', views.postEvent),
]