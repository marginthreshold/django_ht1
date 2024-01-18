from django.core.management import BaseCommand
from myhometasks.models import Client


class Command(BaseCommand):
    help = "Create Client."

    def handle(self, *args, **kwargs):
        client = Client(name='Freddy', email='Kruger@knifehands.com', phone_numb='+1313131313', address='Elm str 12')

        client.save()
        self.stdout.write(f'{client}')
