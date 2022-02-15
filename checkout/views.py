from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KJbMGIwYBgg8NCgFTNu5iP3vU1PSbXabTY2eKz78hSnM7moULIEyqUCCT2xRBI6lwHLD86ob2WdhuvvguIrKK3Z00SRxS5258',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)