from django.shortcuts import render
from .models import Product


def all_products(request):
    # Shows all products, will include sorting and search queries as well

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
