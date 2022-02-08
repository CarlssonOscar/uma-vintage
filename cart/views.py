from django.shortcuts import render, redirect

# Create your views here.

def view_cart(request):
    """ Render cart content """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a product to the cart """

    piece = int(request.POST.get('piece'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] = piece

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)