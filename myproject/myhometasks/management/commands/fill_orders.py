import random
from random import randint, sample
from django.core.management.base import BaseCommand
from myhometasks.models import Client, Product, Order, OrderProduct


class Command(BaseCommand):
    help = "Generate orders."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count of orders')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for _ in range(count + 1):
            client = Client.objects.filter(pk=randint(4, 10)).first()
            products = random.sample(list(Product.objects.all()), k=randint(1, 6))
            print(products)

            order = Order.objects.create(customer=client, total_price=0.00)
            total_price = 0.00

            for product in products:
                quantity = randint(1, 11)
                price = float(product.price)
                print(type(price))
                total_price += quantity * price
                print(quantity, price, total_price)

                order_product = OrderProduct.objects.create(order=order, product=product, quantity=quantity)

            order.product = order_product
            order.total_price = total_price
            order.save()
