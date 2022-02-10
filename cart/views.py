from django.shortcuts import render, redirect, HttpResponse

# Create your views here.


def view_cart(request):
    """ Render cart content """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add products to the cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def delete_from_cart(request, item_id):
    """Delete the item from the shopping bag"""
    cart = request.session.get('cart', {})   
    cart.pop(item_id)
    request.session['cart'] = cart
    return HttpResponse(status=200)
