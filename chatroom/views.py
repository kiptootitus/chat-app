from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render

def handler404(request, exception):
    
    return render(request, '404.html', status=404)
  
def main(request):
    print(request.headers)
    return render(request, 'main.html', {})

def messages(request):
    context = {'foo': 'bar',}
    return render(request, 'messages.html', context)
