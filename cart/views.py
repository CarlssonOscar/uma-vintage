from django.shortcuts import render

# Create your views here.

def view_cart(request):
    """ Render cart content """

    return render(request, 'cart/cart.html')