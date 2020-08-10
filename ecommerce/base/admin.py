from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin
from ecommerce.base.models import Item, OrderItem, Order


admin.site.register(OrderItem)
admin.site.register(Order)


@admin.register(Item)
class ItemAdmin(OrderedModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
