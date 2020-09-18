from django.urls import path
from django.urls import re_path

from . import views

urlpatterns = [re_path(r'^Login',views.Login,name= 'Login'),
               re_path(r'^chatbox',views.chat,name='chat'),
               re_path(r'^homep',views.homep,name='homep'),
               re_path(r'^Homepage',views.Homepage,name='Homepage'),
               re_path(r'^prsnl',views.prsnl,name='prsnl'),
               re_path(r'^Schedule',views.Schedule_class,name='Schedule_class'),]
