from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mychatapp/index.html')

def detail(request, room_name):
    context = { }
    return render(request, 'mychatapp/detail.html', context)