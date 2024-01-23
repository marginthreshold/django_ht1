from django.core.management.base import BaseCommand
from myhometasks.models import Product


class Command(BaseCommand):
    help = "Generate fake product."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count of products')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            product = Product(name=f'knife_{i}', description=f'{i}cm long knife', price=1+i,
                              quantity=1)
            product.save()
