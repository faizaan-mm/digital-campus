from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

def Login(request):
    template = loader.get_template('screens/Login.html')
    context = {}
    return HttpResponse(template.render(context, request))

def chat(request):
    template = loader.get_template('screens/chatbox intro.html')
    context = {}
    return HttpResponse(template.render(context, request))

def homep(request):
    template = loader.get_template('screens/homep_enroll.html')
    context = {}
    return HttpResponse(template.render(context, request))

def Homepage(request):
    template = loader.get_template('screens/Homepage.html')
    context = {}
    return HttpResponse(template.render(context, request))
    
def prsnl(request):
    template = loader.get_template('screens/prsnl_dtls.html')
    context = {}
    return HttpResponse(template.render(context, request))

def Schedule_class(request):
    template = loader.get_template('screens/Schedule class.html')
    context = {}
    return HttpResponse(template.render(context, request))