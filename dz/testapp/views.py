from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def base(request):
    return render(request,'base.html')
def top(request):
    return render(request,'top-sellers.html')