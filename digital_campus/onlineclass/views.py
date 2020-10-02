from .models import *
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login as auth_login, logout
import csv, io

def Login(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')  # Get username and password
        password = request.POST.get('password')  # from the form
        user = authenticate(username=userid, password=password)
        request.session['user'] = user

        if user:  # Check if user exists
            if user.is_active:  # Check if user is active
                auth_login(request, user)
                if user.user_type == 3:
                    return redirect('onlineclass:studenthome')
                elif user.user_type == 2:
                    return redirect('onlineclass:teacherhome')
                else:
                    print("not student")
                    return HttpResponseRedirect(reverse('index'))
            else:
                error_message = "*Account Not Active"
                return render(request, 'Login.html', {'error_message': error_message})
        else:
            error_message = "*Invalid Login Credentials"
            return render(request, 'Login.html', {'error_message': error_message})
    else:
        return render(request, 'Login.html')

def chat(request):
    template = loader.get_template('chatbox intro.html')
    context = {}
    return HttpResponse(template.render(context, request))

def homep(request):
    template = loader.get_template('homep_enroll.html')
    context = {}
    return HttpResponse(template.render(context, request))

def index(request):
    if request.user.is_authenticated:
        template = loader.get_template('Homepage.html')
        context = {}
        return HttpResponse(template.render(context, request))
    else:
        return redirect('onlineclass:Login')
    
def prsnl(request):
    template = loader.get_template('prsnl_dtls.html')
    context = {}
    return HttpResponse(template.render(context, request))

def Schedule_class(request):
    template = loader.get_template('Schedule class.html')
    context = {}
    return HttpResponse(template.render(context, request))

def register(request):
    if request.method == 'POST':
        f = request.FILES
        utype = int(request.POST.get('type'))
        data_set = f['file1'].read().decode('UTF-8')
        for i in data_set.split():
            print(data_set)
            student = i.split(',')
            if utype == 3:
                campus = Campus.objects.filter(name=student[6]).first()
                newUser = User(username = student[0], email = student[1], password = make_password(student[0]+student[5]), user_type = 3, campus = campus)
                newUser.save()
                section = Section.objects.filter(pk=student[4]).first()
                newStud = Student(user = newUser, section = section, birth_date = student[5])
                newStud.save()
            if utype == 2:
                print(student)
                campus = Campus.objects.filter(name=student[6]).first()
                newUser = User(username = student[0], email = student[1], password = make_password(student[0]+student[7]), user_type = 2, campus = campus)
                newUser.save()
                dept = Department.objects.filter(name=student[3]).first()
                newStud = Faculty(user = newUser, dept = dept, designation = student[4], qualifications = student[5], birth_date=student[7])
                newStud.save()
            
        return render(request, 'homep_enroll.html')
    else:
        return render(request, 'homep_enroll.html')

def scheduletest(request):
    template = loader.get_template('scheduletest.html')
    context = {}
    return HttpResponse(template.render(context, request))
    
@login_required
def Logout(request):
    logout(request)
    return redirect('onlineclass:Login')

@login_required
def studenthome(request):
    if request.user.is_authenticated:
        template = loader.get_template('studenthome.html')
        context = {}
        return HttpResponse(template.render(context, request))
    else:
        return redirect('onlineclass:Login')

@login_required
def teacherhome(request):
    if request.user.is_authenticated:
        template = loader.get_template('teacherhome.html')
        context = {}
        return HttpResponse(template.render(context, request))
    else:
        return redirect('onlineclass:Login')