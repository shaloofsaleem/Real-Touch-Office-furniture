from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from .models import * 
# Create your views here.


def  LoginPage(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user_object = User.objects.filter(username = email)
        if not user_object.exists():
            messages.warning(request,'Account not Found')
            return HttpResponseRedirect(request.path_info)
        
        if not user_object[0].profile.is_mail_verified:
            messages.warning(request,'Account is not verified')
            return HttpResponseRedirect(request.path_info)
        
        user_object= authenticate(username = email,password=password)
        if user_object:
            login(request,user_object)
            return redirect('/')

        messages.warning(request,'Invalide credentials. ')
        return HttpResponseRedirect(request.path_info)

    return render(request,'User-Template/accounts/login_form.html')

def  SignupPage(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        
        
        user_object = User.objects.filter(username = email)
        if user_object.exists():
            messages.warning(request,'Email is already taken')
            return HttpResponseRedirect(request.path_info)
        
        user_object= User.objects.create(first_name = first_name, last_name = last_name, email= email, username =email)
        user_object.set_password(password)
        user_object.save()

        messages.warning(request,'An Email has been send Your Email. ')
        return HttpResponseRedirect(request.path_info)


    
    return render(request,'User-Template/accounts/signup_form.html')    



def activation_mail(request, email_token):
    try:
        user = Profile.objects.get(email_token = email_token)
        user.is_mail_verified = True
        user.save()
        return redirect('/')
    except :
        return HttpResponse("Invalide Email token")
