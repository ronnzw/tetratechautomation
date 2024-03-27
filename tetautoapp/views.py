from django.shortcuts import render, redirect
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse

from .forms import ContactForm


def home(request):
    return render(request,'tetautoapp/home.html',{})

def about(request):
    return render(request,'tetautoapp/about.html',{})

def ourServices(request):
    return render(request,'tetautoapp/OurServices.html',{})

def cliental(request):
    return render(request,'tetautoapp/cliental.html')

def success(request):
    return render(request,'tetautoapp/Success.html',{})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('topic')
            email_address = form.cleaned_data.get('email')
            client_name = form.cleaned_data.get('name')
            message = form.cleaned_data.get('message')
            company = form.cleaned_data.get('company')
            phone = form.cleaned_data.get('phone_number')
            full_message = f"""
            ________________________
            A message has been received from your website www.tetratechautomation.co.zw.
            Here are the client details below 
            Client name: {client_name}
            Client company(if any): {company}, 
            contact number: {phone}
            email address: {email_address}
            ________________________
            Below is the message from the client
            ________________________


            {message}
            """
            try:
                send_mail(subject=subject,
                          message = full_message,
                          from_email="info@tetratechautomation.co.zw",
                          recipient_list=["info@tetratechautomation.co.zw"],
                          )
            except BadHeaderError:
                return HttpResponse("Invalid header found")
            return redirect('/success')
        else:
            cxt = {'form': form}
            return render(request, 'tetautoapp/contact.html', cxt)  # Redirect to a success page
    else:
        form = ContactForm()
    return render(request, 'tetautoapp/contact.html', {'form': form})

# Create your views here.
