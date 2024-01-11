from django.shortcuts import render,redirect
from .models import *
from .forms import *
from morefeature.models import *
from product.models import *
from django.db.models import Q  # New
from django.contrib import messages


# Create your views here.

def Base(request):
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
    
    return render(request,'User-Template/base-layout.html',context)


def homepage(request):
    slider = Slider.objects.all().order_by('-id')[:4]
    hero = Hero.objects.all().order_by('-id')[0:1]
    brand = ClientBrand.objects.all().order_by('-id')
    products = Product.objects.all()
    if request.method == "GET":
        form = SubscribeForm()
    else:
        form = SubscribeForm(request.POST)
        if form.is_valid():
            data=ContactMessage()
            data.email = form.cleaned_data["email"]
            data.save()
            messages.success(request, 'Your are Subscribe successfully sent!')
            return redirect('/')
    form = SubscribeForm()    
    context={
        'slider' :slider,
        'hero':hero,
        'brand' : brand,
        'products':products,
        'form': form,
    }
    return render(request,'User-Template/Landing-page/home_page.html',context)

def Search(request):
    print(request.POST)
    query = request.POST['query']
    product =Product.objects.filter(status=True,title__icontains=query)
    context = {
        'product':product
    }
    return render(request,'User-Template/Landing-page/search.html',context)