from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('all/', views.allEvent),
    path('post/', views.postEvent),
    path('id/',views.getEvent),
]