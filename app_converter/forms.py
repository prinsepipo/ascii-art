from django import forms


class ImageUploadForm(forms.Form):
    image = forms.ImageField()
    ascii_characters = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': '.xcv&#@'
    }))
