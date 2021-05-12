from django.conf import settings

from sorl.thumbnail import get_thumbnail


def create_thumb(image):
    for size in settings.THUMBNAIL_PRODUCT_SIZES:
        get_thumbnail(image, size, format='JPEG', colorspace="RGB", crop='center', quality=settings.THUMBNAIL_QUALITY)
