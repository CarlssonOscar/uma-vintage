from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from checkout.models import Order
from .models import Profiles
from .forms import ProfilesForm
from django.contrib.auth.decorators import login_required


def profile(request):
    """ Display user profiles. """
    profile = get_object_or_404(Profiles, user=request.user)

    if request.method == 'POST':
        form = ProfilesForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.info(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           'Update failed. Please ensure the form is valid.')
    else:
        form = ProfilesForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def past_orders(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
