from django.urls import path
from . import views

app_name = 'onlineclass'

urlpatterns = [
    path('login/',views.Login,name= 'Login'),
    path('logout/',views.Logout,name= 'Logout'),
    path('chatbox/',views.chat,name='chat'),
    path('homep/',views.homep,name='homep'),
    path('prsnl/',views.prsnl,name='prsnl'),
    path('Schedule/',views.Schedule_class,name='Schedule_class'),
    path('register/',views.register,name='register'),
    path('scheduletest/',views.scheduletest,name='scheduletest'),
    path('studenthome/',views.studenthome,name='studenthome'),
    path('teacherhome/',views.teacherhome,name='teacherhome'),
]
