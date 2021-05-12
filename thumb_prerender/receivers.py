from django.db.models.signals import pre_save
from django.dispatch import receiver

from oscar.core.loading import get_model

from thumb_prerender.utils import create_thumb

ProductImage = get_model('catalogue', 'ProductImage')


@receiver(pre_save, sender=ProductImage)
def product_image_pre_save(sender, **kwargs):
    image = kwargs['instance'].original
    create_thumb(image)
