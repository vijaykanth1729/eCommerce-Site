import os

from django.shortcuts import render
from .models import ProductImage, Product
from django.http import Http404
def home(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'products/home.html', context)

def single(request,slug):
    try:
        product = Product.objects.get(slug=slug)
        images = ProductImage.objects.filter(product=product)

        #images = product.productimage_set.all()
        # new_img = []
        # for img in images:
        #     new_img.append("media/"+ str(img.image))
        # print(type(new_img))
        # data = str(new_img)
        # data = data
        context = {'product':product, 'images':images}
    except Product.DoesNotExist:
        raise Http404
    return render(request, 'products/detail.html', context)

def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None
    if q:
        products = Product.objects.filter(title__icontains=q)
        context = {'query':q, 'products':products}

        template = 'products/search.html'
    else:
        context = {}
        template = 'products/home.html'
    return render(request, template, context)

