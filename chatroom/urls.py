from django.urls import path
from . import views


handler404 = 'chatroom.views.handler404'

urlpatterns = [
    path('', views.main, name='main'),
    path('chatroom/', views.members, name='chatroom'),
]
