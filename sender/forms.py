from dal import autocomplete
from django import forms
from .models import EmailMessage


class EmailMessageForm(forms.ModelForm):
    class Meta:
        model = EmailMessage
        fields = '__all__'
        widgets = {
            'recipients': autocomplete.ModelSelect2Multiple(url='recipient-autocomplete')
        }
