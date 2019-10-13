from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, Http404

import os

from .forms import ImageUploadForm
from .models import RawImage, AsciiImage


def index(request):
    context = {}
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            RawImage.objects.all().delete()
            raw_image = RawImage()
            raw_image.image = form.cleaned_data['image']
            raw_image.ascii_characters = form.cleaned_data['ascii_characters']
            raw_image.save()
            context['raw_image'] = raw_image.image
            context['converted_image'] = AsciiImage.objects.get(
                raw=raw_image).image

    form = ImageUploadForm()
    context['form'] = form

    return render(request, 'index.html', context)
