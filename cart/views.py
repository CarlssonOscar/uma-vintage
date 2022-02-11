from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


def view_cart(request):
    """ Render cart content """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add products to the cart """
    
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {product.name} to cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def delete_from_cart(request, item_id):
    """Delete the item from the shopping bag"""
    product = get_object_or_404(Product, pk=item_id)
    cart = request.session.get('cart', {})   
    cart.pop(item_id)
    messages.success(request, f'Removed {product.name} from your bag')
    
    request.session['cart'] = cart
    return HttpResponse(status=200)
