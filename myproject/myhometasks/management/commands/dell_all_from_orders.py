from django.core.management.base import BaseCommand
from myhometasks.models import Client, Product, Order, OrderProduct


class Command(BaseCommand):
    help = "Delete all from orders tables."

    def handle(self, *args, **kwargs):
        Order.objects.all().delete()
        OrderProduct.objects.all().delete()
