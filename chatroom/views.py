from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import chatroom

def members(request):
  chatrooms = chatroom.objects.all().values()
  template = loader.get_template('mysite.html')
  context = {
    'chatroom': chatrooms,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())


