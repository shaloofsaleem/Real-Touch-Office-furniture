from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(BodyAbout)
class CategoryAdmin(admin.ModelAdmin):
        list_display = [
        'OurVision','is_active',
]
@admin.register(Clients)
class CategoryAdmin(admin.ModelAdmin):
        list_display = [
        # 'OurVision','parent_id','description','is_active',
        ]
@admin.register(CustomerSay)
class CustomerSayAdmin(admin.ModelAdmin):
        list_display = [
        # 'OurVision','parent_id','description','is_active',
        ]
@admin.register(ClientBrand)
class ClientBrandAdmin(admin.ModelAdmin):
        list_display = [
         'name',
        ]    

class ContactAdmin(admin.ModelAdmin):
        list_display = ['name','subject','modified_date','status' ]
        readonly_fields=('name','subject','email','message','phone_no','file')
        list_filter=['status']                
admin.site.register(ContactMessage ,ContactAdmin)
class customizeAdmin(admin.ModelAdmin):
        list_display = ['name' ]
        readonly_fields=('name',)
               
admin.site.register(customize,customizeAdmin)
class SubscribAdmin(admin.ModelAdmin):
        list_display = ['email' ]
        readonly_fields=('email',)
admin.site.register(Subscription,SubscribAdmin)