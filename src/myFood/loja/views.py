from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Category, Marca, Size, Product, ProductAttribute

# Create your views here.

def index(request):
    return render(request, 'index.html')

@login_required
def category_list(request):
    data = Category.objects.all().order_by('-id')
    return render(request, 'category_list.html', {'data': data})

@login_required
def marca_list(request):
    data = Category.objects.all().order_by('-id')
    return render(request, 'marca_list.html', {'data': data})
    

@login_required
def cart(request):
    cart_id = request.session.get('cart_id', None)
    if cart is not None:
         print('create new cart')
         request.session['cart_id'] = cart.id
    else:
        print('Cart ID exists')

    return render(request, "cart.html",{})

def search(request):
    return render(request, 'search.html')



def product_list(request):
    data = Product.objects.all().order_by('-id')
    cats = Product.objects.distinct().values('category__title')
    marcas= Product.objects.distinct().values('marca__title')
    sizes= ProductAttribute.objects.distinct().values('size__title')
    return render(request, 'product_list.html', {'data': data, 'cats': cats, 'marcas': marcas, 'sizes': sizes})

@login_required
def size_list(request):
    data = Category.objects.all().order_by('-id')
    return render(request, 'size_list.html', {'data': data})

