from django.conf import settings
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.files.storage import default_storage as storage

from .models import AsciiImage, RawImage
from utils.converter import ImageConverter

from .choices import FILTER_CHOICES


import uuid
import urllib.request
import io


@receiver(post_save, sender=RawImage)
def convert_image(sender, instance, **kwargs):
    image_url = instance.image.url
    fp = io.BytesIO(urllib.request.urlopen(image_url).read())
    mfilter = FILTER_CHOICES[int(instance.filters) - 1][1]

    converter = ImageConverter()
    converter.characters = instance.ascii_characters or '.@'
    converter.filter = mfilter.lower()
    image = converter.process_image(fp)
    filename = str(uuid.uuid4()) + '.png'
    new_file_path = settings.MEDIA_ROOT + '/converted/' + filename

    buffer = io.BytesIO()
    image.save(buffer, format='PNG')
    imageFile = storage.open('converted/' + filename, 'wb')
    imageFile.write(buffer.getvalue())
    imageFile.flush()
    imageFile.close()

    ascii_image = AsciiImage()
    ascii_image.raw = instance
    ascii_image.image = 'converted/' + filename
    ascii_image.save()


@receiver(post_delete, sender=RawImage)
def delete_image_in_storage(sender, instance, **kwargs):
    instance.image.delete(save=False)


@receiver(post_delete, sender=AsciiImage)
def delete_ascii_images(sender, instance, **kwargs):
    instance.image.delete(save=False)
