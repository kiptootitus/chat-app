from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatroom, name='index'),
    path('404/', views.error_404, name='404')
]
