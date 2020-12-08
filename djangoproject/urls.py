"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from djtot import views
from dbt import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.hello),
    path('about/',views.about),
    path('rcd/<str:name>/',views.rc),
    path('tb/<int:n>/',views.tb),
    path('tb/<str:name>/<int:age>/',views.rcds),
    path('de/',views.sample),
    path('login/',views.login),
    path('register/',views.register),
    path('js/',views.js),
    path('arit/',views.arit),
    path('',v.home),
    path('lrbt/',v.lrbttask),


]
