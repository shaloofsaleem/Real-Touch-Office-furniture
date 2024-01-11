from django.urls import path
from . import views as v

# app_name = 'product'
urlpatterns = [
    path('products/',v.Product_List,name="product_list"),
    path('products/<int:id>/<slug:slug>', v.Product_detail, name='product_detail'),
    path('ajaxmatrial/', v.AjaxMatrial, name='ajaxmatrial'),
    path('wishlist/', v.Wishlist, name='wishlist'),

     
]