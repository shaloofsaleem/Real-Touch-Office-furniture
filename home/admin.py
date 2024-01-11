from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
        list_display = [
        'images','text','discription','is_active',
        ]

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
        list_display = [
          'image','subtitle','header1','header2','is_active'
        ]
        