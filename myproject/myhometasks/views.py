from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import logging

from django.core.files.storage import FileSystemStorage

from .models import Client, OrderProduct, Product, Order
from datetime import datetime, timedelta
from .forms import PhotoForm

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Main page accessed')
    return render(request, 'mainpg.html')


def about(request):
    logger.info(f'About page was visited')
    return render(request, 'aboutme.html')


def client_orders(request, client_id, last_days):
    client = get_object_or_404(Client, pk=client_id)
    start_period = datetime.now() - timedelta(days=last_days)
    orders = Order.objects.filter(customer=client, date_ordered__gte=start_period)
    orders_data = []

    for order in orders:
        product_names = []

        products_in_order = OrderProduct.objects.filter(order=order)
        for product_in_order in products_in_order:
            product_name = Product.objects.filter(id=product_in_order.product_id)
            product_names.append([item.name for item in product_name])
            product_names.append(product_in_order.quantity)

        orders_data.append({'order': order, 'product_names': product_names,
                            'total_price': order.total_price})

        return render(request, 'myhometasks/client_orders.html', {'orders_data': orders_data, 'client': client})


def upload_image(request):
    if request.method == 'POST':

        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.cleaned_data['product']
            product.image = form.cleaned_data['image']
        product.save()
        form.save
    else:
        form = PhotoForm()
    return render(request, 'myhometasks/upload_image.html', {'form': form})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'myhometasks/product_list.html', {'products': products})
