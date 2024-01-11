from django.contrib import admin
from .models import *
import admin_thumbnails
import admin_thumbnails
# Register your models here.


@admin_thumbnails.thumbnail('image')
class ProductImageInline(admin.TabularInline):
    model = Images
    readonly_fields = ('id',)
    extra = 1

class ProductVariantsInline(admin.TabularInline):
    model = Variants
    readonly_fields = ('image_tag',)
    extra = 1
    show_change_link = True






@admin_thumbnails.thumbnail('image')
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['image','title','id','image_thumbnail']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','category','id', 'status','image_tag']
    list_filter = ['category']
    readonly_fields = ('image_tag',)
    inlines = [ProductImageInline,ProductVariantsInline]
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject','comment', 'status','create_at']
    list_filter = ['status']
    readonly_fields = ('subject','comment','ip','user','product','rate','id')

class MetrialAdmin(admin.ModelAdmin):
    list_display = ['title','id','image','discription','is_active']

class SizeAdmin(admin.ModelAdmin):
    list_display = ['name','code']


class VariantsAdmin(admin.ModelAdmin):
    list_display = ['title','product','metrial','size','price','quantity','image_tag']

class ProductLangugaeAdmin(admin.ModelAdmin):
    list_display = ['title','lang','slug']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['lang']

class CategoryLangugaeAdmin(admin.ModelAdmin):
    list_display = ['title','lang','slug']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['lang']


admin.site.register(Product,ProductAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Images,ImagesAdmin)
admin.site.register(Metrial,MetrialAdmin)
admin.site.register(Size,SizeAdmin)
admin.site.register(Variants,VariantsAdmin)
admin.site.register(Wishlist)
