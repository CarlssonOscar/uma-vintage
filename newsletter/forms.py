from django import forms
from .models import Newsletter


class NewsletterForm(forms.ModelForm):
    email = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={'placeholder': 'Newsletter sign up!'}))
    class Meta:
        model = Newsletter
        fields = ('email',)

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
