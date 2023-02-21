from django.urls import path
from . import views




urlpatterns = [
    path('chatroom/', views.chatroom, name='chatroom'),
    path('templates/', views.error_404, name='404')
] 