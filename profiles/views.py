from django.shortcuts import render, get_object_or_404
from .models import Profiles
from .forms import ProfilesForm

def profile(request):
    """ Display user profiles. """
    profile = get_object_or_404(Profiles, user=request.user)
    
    form = ProfilesForm(instance=profile)
    orders = profile.orders.all()
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)
