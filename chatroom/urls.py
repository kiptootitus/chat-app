from django.urls import path
from . import views




urlpatterns = [
    path('', views.main, name='mysite'),
    path('chatroom/', views.messages, name='Messages')
]
