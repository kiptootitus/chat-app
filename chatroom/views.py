from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Chatroom, Message

@login_required
def chatroom_view(request, chatroom_id):
    # Get the chatroom object for the given ID
    chatroom = Chatroom.objects.get(id=chatroom_id)
    
    # Get the list of messages for this chatroom
    messages = Message.objects.filter(chatroom=chatroom)
    
    # Render the template with the chatroom and message data
    return render(request, 'chatroom.html', {
        'chatroom': chatroom,
        'messages': messages,
    })
