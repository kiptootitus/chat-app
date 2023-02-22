from django.urls import path
from . import views




urlpatterns = [
    path('', views.main, name='mysite'),
    path('', views.handler404, name='404'),
    path('chatroom/', views.messages, name='Messages')
]
