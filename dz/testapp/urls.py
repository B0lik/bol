from django.urls import path
from django.contrib import admin
from .views import index,top,base

urlpatterns =[
    path('', index),
    path('',base),
    path('',top),
]