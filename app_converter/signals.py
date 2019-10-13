from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import RawImageFile
from utils.converter import convert_image_to_ascii


@receiver(post_save, sender=RawImageFile)
def convert_image(sender, instance, **kwargs):
    fp = instance.image.path
    image = convert_image_to_ascii(fp)
    image.save(fp, format='PNG')


@receiver(post_delete, sender=RawImageFile)
def delete_image_in_storage(sender, instance, **kwargs):
    instance.image.delete(save=False)
