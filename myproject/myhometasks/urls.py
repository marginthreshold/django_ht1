from django.urls import path
from . import views
from .views import client_orders, upload_image, product_list

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('orders/<int:client_id>/<int:last_days>/', client_orders, name='client_orders'),
    path('upload/', upload_image, name='upload_image'),
    path('product_list/', product_list, name='product_list'),
]
