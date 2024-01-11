from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from .models import *
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def Customisation(request):
    data = customize.objects.all()
    
    context ={
        'data' : data
      
    }
    return render(request,'User-Template/Customisation/custom.html',context)
def About(request):
    about =BodyAbout.objects.all()
    brand = ClientBrand.objects.all().order_by('-id')
    context ={
        'about':about,
        'brand':brand       
    }
    return render(request,'User-Template/About/about.html',context)


def Contact(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            data=ContactMessage()
            data.name = form.cleaned_data['name']
            data.phone_no =form.cleaned_data['phone_no']
            data.subject = form.cleaned_data["subject"]
            data.email = form.cleaned_data["email"]
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, 'Your message was successfully sent!')
            return redirect('feature:contact')
    form = ContactForm()    
    context={"form": form}
    return render(request, "User-Template/Contact/contact.html",context)

def Project(request):
    return render (request,'User-Template/Project/project.html')