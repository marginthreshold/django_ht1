from django.urls import path
from . import views
from .views import client_orders

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('orders/<int:client_id>/<int:last_days>/', client_orders, name='client_orders'),
]