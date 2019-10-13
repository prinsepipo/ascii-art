from django.contrib import admin

from .models import AsciiImage, RawImage


admin.site.register(AsciiImage)
admin.site.register(RawImage)
