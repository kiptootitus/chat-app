# chatroom/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('chatrooms')
    else:
        form = AuthenticationForm()
    return render(request, 'chatroom/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'chatroom/register.html', {'form': form})

# Create views to display and create chat rooms:
def chatrooms_view(request):
    chatrooms = ChatRoom.objects.all()
    return render(request, 'chatroom/chatrooms.html', {'chatrooms': chatrooms})

def create_chatroom_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        chatroom = ChatRoom.objects.create(name=name)
        return redirect('chatroom', chatroom.id)
    return render(request, 'chatroom/create_chatroom.html')

# Create views to display and send messages within a chat room:
def chatroom_view(request, chatroom_id):
    chatroom = ChatRoom.objects.get(id=chatroom_id)
    messages = chatroom.message_set.order_by('-timestamp')[:50]
    return render(request, 'chatroom/chatroom.html', {'chatroom': chatroom, 'messages': messages})

def send_message_view(request, chatroom_id):
    chatroom = ChatRoom.objects.get(id=chatroom_id)
    text = request.POST.get('text')
    message = Message.objects.create(user=request.user, chatroom=chatroom, text=text)
    return redirect('chatroom', chatroom.id)
