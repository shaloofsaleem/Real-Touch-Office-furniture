from django.contrib import admin

# Register your models here.

from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
        list_display = [
        'name','parent_id','description','slug','is_active',
        ]
        list_filter=['is_active']
# @admin.register(Metrial)
# class MetrialAdmin(admin.ModelAdmin):
#         list_display=['title','image','discription','is_active']
# @admin.register(Size)           
# class SizeAdmin(admin.ModelAdmin):
#         list_display=['Size','discription','is_active',]         