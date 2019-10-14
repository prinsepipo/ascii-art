from django.db import models

from .choices import FILTER_CHOICES


class RawImage(models.Model):
    image = models.ImageField(upload_to='raw/')
    ascii_characters = models.CharField(max_length=200, null=True, blank=True)
    filters = models.IntegerField(choices=FILTER_CHOICES, default=1)

    def __str__(self):
        return f'Raw Image {self.id}'


class AsciiImage(models.Model):
    raw = models.ForeignKey(
        RawImage, on_delete=models.CASCADE, related_name='raw')
    image = models.ImageField(upload_to='converted/')

    def __str__(self):
        return f'Image {self.id}'
