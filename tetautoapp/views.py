from django.shortcuts import render, redirect
from .forms import ContactForm


def home(request):
    return render(request,'tetautoapp/home.html',{})

def about(request):
    return render(request,'tetautoapp/about.html',{})

def ourServices(request):
    return render(request,'tetautoapp/OurServices.html',{})

def cliental(request):
    return render(request,'tetautoapp/cliental.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = ContactForm()
    return render(request, 'tetautoapp/contact.html', {'form': form})

# Create your views here.
