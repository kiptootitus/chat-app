# chatroom/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('chatrooms/', chatrooms_view, name='chatrooms'),
    path('chatroom/create/', create_chatroom_view, name='create_chatroom'),
    path('chatroom/<int:chatroom_id>/', chatroom_view, name='chatroom'),
    path('chatroom/<int:chatroom_id>/send_message/', send_message_view, name='send_message'),
]

