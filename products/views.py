from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    # Shows all products, will include sorting and search queries as well

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)



def product_details(request, product_id):
    # Shows details of a product 

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)
