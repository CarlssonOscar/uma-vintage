from django import forms
from .models import Newsletter


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ('email',)

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            placeholders = {
            'email': 'Please sign up to our newsletter!',
            }