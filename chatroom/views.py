from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import members
from django.shortcuts import render

def handler404(request, exception):
    return render(request, '404.html', status=404)
  
def member(request):
  member = members.objects.all().values()
  template = loader.get_template('mysite.html')
  context = {
    'members': member,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())


