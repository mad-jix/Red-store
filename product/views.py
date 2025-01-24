from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect,get_list_or_404

from .models import Products

# Create your views here.
def products(request):
    products_list = {'products': Products.objects.all()}
    return render(request, 'products.html', products_list)


def product_details(request,pk):
    product = get_list_or_404(Products,pk=pk)
    print('iage',product)
    return render(request,'product_details.html',{'product':product}) 