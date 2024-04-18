from django.dispatch import receiver
from django.db.models.signals import post_delete
from .models import Image,document
from django.conf import settings
import os

#تابع عذف عکس از از محل ذخیره بعد از حذف رکورد همون عکس
@receiver(post_delete, sender=Image)
def delete_product_image(sender, **kwargs):
    path = settings.MEDIA_ROOT + str(kwargs['instance'].path)
    if os.path.isfile(path):
        os.remove(path)

#تابع عذف داکیومنت از از محل ذخیره بعد از حذف رکورد همون داکیومنت
@receiver(post_delete, sender=document)
def delete_product_document(sender, **kwargs):
    path = settings.MEDIA_ROOT + str(kwargs['instance'].path)
    if os.path.isfile(path):
        os.remove(path)
