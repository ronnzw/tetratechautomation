from django.shortcuts import render


def home(request):
    return render(request,'tetautoapp/home.html',{})

def about(request):
    return render(request,'tetautoapp/about.html',{})

def ourServices(request):
    return render(request,'tetautoapp/OurServices.html',{})
# Create your views here.
