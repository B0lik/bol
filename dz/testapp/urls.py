from django.urls import path
from django.contrib import admin
from .views import index,base,top

urlpatterns =[
    path('', index),
    path('',base),
    path('',top),
]