from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

def login(request):
    template = loader.get_template('screens/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
