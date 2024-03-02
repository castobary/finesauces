from django.shortcuts import render
from .models import Category, Product

# Create your views here.

def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    return render(
        request, 'listings/product_list.html',
       context = {
            'categories': categories,
            'products': products
        }
    )