from django.urls import path
from . import views as v

app_name = 'custom'
urlpatterns = [
    path('category/<uuid:id>/',v.ProductCategoryList,name='category')

     
]