from django.apps import AppConfig


class ReadingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'readings'

    def ready(self):
        from .signals import create_profile, save_profile

class MyAppConfig(AppConfig):
    name = 'myapp'
    verbose_name = 'My App'

    def ready(self):
        from .management.commands.bulk_create_cards import Command as BulkCreateCardsCommand 
        self.add_command('bulk_create_cards', BulkCreateCardsCommand())
