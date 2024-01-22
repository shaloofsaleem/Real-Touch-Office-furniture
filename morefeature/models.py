from django.db import models
from autoslug import AutoSlugField
from django.forms import TextInput, Textarea,ClearableFileInput
from django.forms import ModelForm
import uuid
from django.urls import reverse



# Create your models here.
class BodyAbout(models.Model):
    image1         =   models.ImageField(upload_to='about-image/', null=True, blank=True,)
    image2         =   models.ImageField(upload_to='about-image/', null=True, blank=True,)
    OurVision    =   models.CharField(max_length=300)
    OurMission =   models.CharField(max_length=255)
    WhoWeAre    =   models.CharField(max_length=255)
    slug            =   AutoSlugField(populate_from='OurVision',max_length=255,unique=True,null=True )
    is_active       =   models.BooleanField(default=True)
    created_date    =   models.DateTimeField(auto_now_add=True)
    modified_date   =   models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.OurVision

class Clients(models.Model):
    HappyCustomer         =   models.IntegerField()
    YearsinBusiness         =   models.IntegerField()
    ReturnClients    =  models.IntegerField()
    AwardsWon =   models.IntegerField()
    slug            =   AutoSlugField(populate_from='HappyCustomer',max_length=255,unique=True,null=True )
    is_active       =   models.BooleanField(default=True)
    created_date    =   models.DateTimeField(auto_now_add=True)
    modified_date   =   models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.HappyCustomer

class CustomerSay(models.Model):
    name    =   models.CharField(max_length=200)
    image         =   models.ImageField(upload_to='customer-image/', null=True, blank=True,)
    message   =   models.CharField(max_length=300)
    is_active       =   models.BooleanField(default=True)
    created_date    =   models.DateTimeField(auto_now_add=True)
    modified_date   =   models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.name


class ClientBrand(models.Model):
    name    =   models.CharField(max_length=200)
    image         =   models.ImageField(upload_to='Brand-image/', null=True, blank=True,)
    is_active       =   models.BooleanField(default=True)
    created_date    =   models.DateTimeField(auto_now_add=True)
    modified_date   =   models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    STATUS =(
        ('New','New'),
        ('Read','Read'),
        ('Closed','Closed')
    )
    name      = models.CharField(blank=True, max_length=250)
    phone_no  = models.CharField(blank=True, max_length=50)
    email = models.EmailField(blank=True,max_length=50 )
    company= models.CharField(blank= True, max_length=50 )
    subject = models.CharField(blank=True, max_length=255)
    file = models.FileField(blank=True,)
    message = models.TextField(blank=True, max_length=550 )
    status = models.CharField(max_length=10,choices=STATUS,default='New')
    is_active       =   models.BooleanField(default=True)
    ip = models.CharField(max_length=20,blank=True)
    note =    models.CharField(blank=True, max_length=255)
    created_date    =   models.DateTimeField(auto_now_add=True)
    modified_date   =   models.DateTimeField(auto_now=True)    


    def __str__(self):
        return self.name
    
class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name','phone_no','email','subject','file','message']
        widgets={
            'name':TextInput(attrs={'class':"form-control", 'id':"cname", 'placeholder':"Name *", }),
            'email':TextInput(attrs={'class':"form-control" ,'id':"cemail" ,'placeholder':"Email *" }),
            'phone_no':TextInput(attrs={'name':"phone_no", 'class':"form-control" ,'id':"cphone", 'placeholder':"Phone"}),
            'company':TextInput(attrs={ 'name':"company", 'class':"form-control", 'id':"csubject" ,'placeholder':"company"}),
            'subject':TextInput(attrs={ 'name':"subject", 'class':"form-control", 'id':"csubject" ,'placeholder':"Subject"}),
            'file' : ClearableFileInput(attrs={ 'name':"files", 'class':"form-control", 'id':"cfiles" }),
            'message':Textarea(attrs={'class':"form-control", 'name':"message" ,'cols':"30" ,'rows':"4", 'id':"cmessage"  ,'placeholder':"Message *"}),

        }


class customize(models.Model):
    name    =   models.CharField(max_length=200)
    image         =   models.ImageField(upload_to='custom-image/', null=True, blank=True,)
    is_active       =   models.BooleanField(default=True)
    created_date    =   models.DateTimeField(auto_now_add=True)
    modified_date   =   models.DateTimeField(auto_now=True)  
    discription      =   models.CharField(blank=True,null=True,max_length=300 )

    def __str__(self):
        return self.name

class Subscription(models.Model):
    email = models.EmailField(blank=True,max_length=50 )
    created_date    =   models.DateTimeField(auto_now_add=True)
    modified_date   =   models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.email

class SubscribeForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['email']
        widgets={
        #     'name':TextInput(attrs={'class':"form-control", 'id':"cname", 'placeholder':"Name *", }),
            'email':TextInput(attrs={'type':'email', 'class':'form-control form-control-white' ,'placeholder':'Enter your Email Address', 'aria-label':'Email Adress'  }),
        #     'phone_no':TextInput(attrs={'name':"phone_no", 'class':"form-control" ,'id':"cphone", 'placeholder':"Phone"}),
        #     'subject':TextInput(attrs={ 'name':"subject", 'class':"form-control", 'id':"csubject" ,'placeholder':"Subject"}),
        #     'file' : ClearableFileInput(attrs={ 'name':"files", 'class':"form-control", 'id':"cfiles" }),
        #     'message':Textarea(attrs={'class':"form-control", 'name':"message" ,'cols':"30" ,'rows':"4", 'id':"cmessage"  ,'placeholder':"Message *"}),

        }


class Category_Metrial(models.Model):
    id               = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name             =   models.CharField(max_length=255,db_index=True)
    image            =   models.ImageField(upload_to='color-image', null=True, blank=True,)
    slug             =   AutoSlugField(populate_from='name',max_length=255,unique=True,null=True)
    description      =   models.TextField(blank=True,null=True)
    parent_id        =   models.ForeignKey('self', on_delete=models.SET_NULL, null=True,blank=True, related_name='category_parent')
    is_active        =   models.BooleanField(default=True)   
    created_date     =   models.DateTimeField(auto_now_add=True)
    modified_date    =   models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('color_detail', kwargs={'slug': self.slug})


class MetrialColorBord(models.Model):
    id               = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name             =   models.CharField(max_length=255,db_index=True)
    image            =   models.ImageField(upload_to='color-image', null=True, blank=True,)
    slug             =   AutoSlugField(populate_from='name',max_length=255,unique=True,null=True)
    description      =   models.TextField(blank=True,null=True)
    is_active        =   models.BooleanField(default=True)   
    created_date     =   models.DateTimeField(auto_now_add=True)
    modified_date    =   models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
