from django.core.management.base import BaseCommand

from oscar.core.loading import get_model

from thumb_prerender.utils import create_thumb

ProductImage = get_model('catalogue', 'ProductImage')


class Command(BaseCommand):
    help = "For creating product image thumbnails"

    def handle(self, *args, **options):
        self.stdout.write("Starting Thumbnail Creation")
        qs = ProductImage.objects.all()

        for i in qs:
            image = i.original
            create_thumb(image)

        self.stdout.write('Successfully updated %s product images\n' % qs.count())
