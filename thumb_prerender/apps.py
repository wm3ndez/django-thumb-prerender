from django.apps import AppConfig


class ThumbPrerenderConfig(AppConfig):
    name = 'thumb_prerender'

    def ready(self):
        from thumb_prerender import receivers