from django import forms

from .choices import FILTER_CHOICES


class ImageUploadForm(forms.Form):
    image = forms.ImageField()
    ascii_characters = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Default: .@'
    }))
    filters = forms.ChoiceField(widget=forms.Select(), choices=FILTER_CHOICES)
