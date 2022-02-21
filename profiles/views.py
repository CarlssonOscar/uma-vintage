from django.shortcuts import render, get_object_or_404
from .models import Profiles

def profile(request):
    """ Display user profiles. """
    profile = get_object_or_404(Profiles, user=request.user)

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)
