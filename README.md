# django-thumb-prerender

This app is intended to be used with django-oscar and sorl-thumbnail.

When a user updates or creates a new Product Image, the thumbnails will be created according to the sizes predefined in settings.

## Instalation

Install using pip:
~~~
pip install -e https://github.com/wm3ndez/django-thumb-prerender
~~~

Or add it to requirements.txt: 
~~~
-e git+https://github.com/wm3ndez/django-thumb-prerender#egg=thumb_prerender
~~~

## Usage
Add to installed apps as: `thumb_prerender`.

Set the thumbnail sizes in setting. Ex:
~~~
THUMBNAIL_PRODUCT_SIZES = ["1x1", "10x10", "x10", ]
~~~

## Manually create all thumbnails

Run: `python manage.py create_product_thumbs`