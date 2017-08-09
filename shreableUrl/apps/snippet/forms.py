from django import forms
from django.forms import ModelForm
from shreableUrl.apps.snippet.models import Snippet

# Create the form class.
class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        fields = ['data','key']
        widgets = {
            'data':forms.Textarea(attrs={'cols': 15, 'rows': 5 }),
        }