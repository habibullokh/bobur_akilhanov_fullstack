from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('group/', views.group, name="group"),
    path('mark/', views.mark, name='mark'),
    path('centerinfo/', views.centerinfo, name='centerinfo'),
]
