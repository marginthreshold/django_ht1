from django.core.management.base import BaseCommand
from myhometasks.models import Client


class Command(BaseCommand):
    help = "Generate fake client."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count of users')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(name=f'Freddy_{i}', email=f'kruger{i}@mail.ru', phone_numb=f'+131313131{i}',
                            address=f'Elm str {i}')
            client.save()
