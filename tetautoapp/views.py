from django.shortcuts import render


def home(request):
    return render(request,'tetautoapp/home.html',{})

# Create your views here.
