from django.contrib import admin
from django.urls import path, include
from onlineclass import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('onlineclass/', include('onlineclass.urls')),
]
