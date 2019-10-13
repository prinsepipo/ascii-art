from django.db import models


class RawImageFile(models.Model):
    image = models.ImageField(upload_to='raw/')

    def __str__(self):
        return f'Image {self.id}'
