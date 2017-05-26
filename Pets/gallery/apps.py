from django.apps import AppConfig


class GalleryConfig(AppConfig):
    name = 'gallery'
    def ready(self):
        #startup code here 
        import gallery.mysignals