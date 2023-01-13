from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . models import category,Product
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.
def allprocat(request,cslug=None):
    cpage=None
    products_list=None
    if cslug!=None:
        cpage = get_object_or_404(category,slug=cslug)
        products_list = Product.objects.all().filter(category=cpage,available=True)
    else:
        products_list = Product.objects.all().filter(available=True)
    paginator=Paginator(products_list,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        products=paginator.page(page)
    except(EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages)

    return render(request,"category.html",{'category':cpage,'products':products})

def prodetail(request, cslug, pslug):
    try:
        products= Product.objects.get(category__slug=cslug,slug=pslug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'products':products})