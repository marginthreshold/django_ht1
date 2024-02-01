from django.contrib import admin
from .models import Order, Client, OrderProduct, Product


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'image']
    ordering = ['name', '-price']
    list_filter = ['adding_date', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта(description)'
    actions = [reset_quantity]


admin.site.register(Order)
admin.site.register(Client)
admin.site.register(OrderProduct)
admin.site.register(Product, ProductAdmin)
