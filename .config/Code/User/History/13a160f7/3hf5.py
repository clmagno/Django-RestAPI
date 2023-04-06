from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.event_list.as_view()),
    path('<int:id>/',views.event_detail.as_view()),
]