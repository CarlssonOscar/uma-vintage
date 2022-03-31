from django.shortcuts import render
from .models import Newsletter
from django.http import HttpResponseRedirect
from .forms import NewsletterForm

# Create your views here.
def newsletters(request):
    
    form_data = {
            'email': request.POST['email'],
    }
    newsletter_form = NewsletterForm(form_data)
    if newsletter_form.is_valid():

        if request.method == "POST":
            form = NewsletterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.info(request, "Thanks for signing up to our Newsletter!")

    context = {
        'email': 'email',
    }
    return render(request, template, context)
    return HttpResponseRedirect(request.path_info)
