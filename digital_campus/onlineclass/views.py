from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

def Login(request):
    template = loader.get_template('Login.html')
    context = {}
    return HttpResponse(template.render(context, request))

def chat(request):
    template = loader.get_template('chatbox intro.html')
    context = {}
    return HttpResponse(template.render(context, request))

def homep(request):
    template = loader.get_template('homep_enroll.html')
    context = {}
    return HttpResponse(template.render(context, request))

def index(request):
    template = loader.get_template('Homepage.html')
    context = {}
    return HttpResponse(template.render(context, request))
    
def prsnl(request):
    template = loader.get_template('prsnl_dtls.html')
    context = {}
    return HttpResponse(template.render(context, request))

def Schedule_class(request):
    template = loader.get_template('Schedule class.html')
    context = {}
    return HttpResponse(template.render(context, request))

def register(request):
    print(request.POST.get('Email ID'))
    template = loader.get_template('Login.html')
    context = {}
    return HttpResponse(template.render(context, request))

def scheduletest(request):
    template = loader.get_template('scheduletest.html')
    context = {}
    return HttpResponse(template.render(context, request))
    

