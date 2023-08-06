from django.shortcuts import render

def index(reguest):
    return render(reguest, 'index.html')

def top(reguest):
    return render(reguest, 'top-sellers.html')

def base(reguest):
    return render(reguest, 'base.html')