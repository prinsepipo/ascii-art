from django.db import models


class RawImage(models.Model):
    image = models.ImageField(upload_to='raw/')
    ascii_characters = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'Raw Image {self.id}'


class AsciiImage(models.Model):
    raw = models.ForeignKey(
        RawImage, on_delete=models.CASCADE, related_name='raw')
    image = models.ImageField(upload_to='converted/')

    def __str__(self):
        return f'Image {self.id}'
