# signals.py

from django.apps import apps
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.core.management import call_command

@receiver(post_migrate)
def run_migrations(sender, **kwargs):
    if sender.name == "your_app_name":
        call_command("makemigrations")
        call_command("migrate")
