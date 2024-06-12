from django.contrib import admin
from .models import Order, OrderItem

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order_placed', 'status', 'payment')
    list_filter = ('status', 'payment', 'order_placed')
    search_fields = ('id', 'user__username', 'first_name', 'last_name')
    list_editable = ('status',)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'price')
    list_filter = ('order__payment', 'order__order_placed', 'order__updated')
    search_fields = ('order__id', 'product__name')

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
