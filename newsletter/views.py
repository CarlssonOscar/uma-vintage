from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Newsletter
from .forms import NewsletterForm


def newsletters(request): 
    if request.method == 'POST':
        newsletter = request.session.get('newsletter', {})

        form_data = {
            'email': request.POST['email'],
        }
        
        newsletter_form = NewsletterForm(form_data)
        if newsletter_form.is_valid():
            newsletter_form.save()
            messages.info(request, "Thanks for signing up to our Newsletter!")

    template = HttpResponseRedirect(request.path_info)
    context = {
        'newsletter_form': newsletter_form,
    }
    return render(request, template, context)
