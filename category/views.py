from django.shortcuts import render
from .models import *
from product.models import *
from django.core.paginator import Paginator

# Create your views here.
def ProductCategoryList(request, id,):
    category = Category.objects.get(id=id)
    products = Product.objects.filter(category=category)
    paginated = Paginator(products, 8)
    page_number = request.GET.get('page') #Get the requested page number from the URL
    
    product = paginated.get_page(page_number)
    context ={
        'category': category, 
        'product': product
            }
    print(category)

    return render(request, 'User-Template\Category\category_detail.html', context)
