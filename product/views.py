from django.shortcuts import render
from .models import*
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.paginator import Paginator



# Create your views here.
def Product_List(request):
    products = Product.objects.all().order_by('-id')
    paginated = Paginator(products, 8)
    page_number = request.GET.get('page') #Get the requested page number from the URL
    
    product = paginated.get_page(page_number)
    context ={
        'product':product,
    }
    return render (request,'User-Template/products/product-list.html',context)



def Product_detail(request,id,slug):
    query = request.GET.get('q')
    # category = Category.objects.all()
    product = Product.objects.get(pk=id)
    products = Product.objects.filter(category=product.category)
    images = Images.objects.filter(product_id=id)
    comments = Comment.objects.filter(product_id=id,status='True')
    context = {'product': product,'products':products,
               'images': images, 'comments': comments,
               }
    if product.variant !="None": # Product have variants
        if request.method == 'POST': #if we select color
            variant_id = request.POST.get('variantid')
            variant = Variants.objects.get(id=variant_id) #selected product by click color radio
            colors = Variants.objects.filter(product_id=id,size_id=variant.size_id )
            sizes = Variants.objects.raw('SELECT * FROM  product_variants  WHERE product_id=%s GROUP BY size_id',[id])
            query += variant.title+' Size:' +str(variant.size) +' Metrial:' +str(variant.metrial)
        else:
            variants = Variants.objects.filter(product_id=id)
            colors = Variants.objects.filter(product_id=id,size_id=variants[0].size_id )
            sizes = Variants.objects.raw('SELECT * FROM  product_variants  WHERE product_id=%s GROUP BY size_id',[id])
            variant =Variants.objects.get(id=variants[0].id)
        context.update({'sizes': sizes, 'colors': colors,
                        'variant': variant,'query': query
                        })
    return render(request,'User-Template\products\product_detailed.html',context)


def AjaxMatrial(request):
    data = {}
    if request.POST.get('action') == 'post':
        size_id = request.POST.get('size')
        productid = request.POST.get('productid')
        colors = Variants.objects.filter(product_id=productid, size_id=size_id)
        context = {
            'size_id': size_id,
            'productid': productid,
            'colors': colors,
        }
        data = {'rendered_table': render_to_string('User-Template/products/color_list.html', context=context)}
        return JsonResponse(data)
    return JsonResponse(data)



def Wishlists(request):
    wishlist = Wishlist.objects.all()
    context ={
        wishlist : 'wishlist'
    }
    return render(request,'User-Template\products\wishlist.html',context )
    