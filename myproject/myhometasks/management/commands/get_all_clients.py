from django.core.management.base import BaseCommand
from myhometasks.models import Client


class Command(BaseCommand):
    help = "Get all clients."

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        self.stdout.write(f'{clients}')