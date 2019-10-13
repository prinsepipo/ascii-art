from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, Http404

import os

from .forms import ImageUploadForm
from .models import RawImageFile


def index(request):
    context = {}
    if request.method == 'POST':
        RawImageFile.objects.all().delete()
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = RawImageFile()
            image.image = form.cleaned_data['image']
            image.save()
            context['converted_image'] = image.image

    return render(request, 'index.html', context)
