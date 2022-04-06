from django.contrib import messages
from .models import Newsletter
from .forms import NewsletterForm


def newsletter_form_emails(request):

    if request.method == 'POST':
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            newsletter_form = NewsletterForm()
            messages.info(request,
                          'Thank you very much for subscribing \
                          to our newsletter')
    else:
        newsletter_form = NewsletterForm()

    context = {
        'newsletter_form': newsletter_form,
    }

    return context
