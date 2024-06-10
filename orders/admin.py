from django.contrib import admin
from .models import Order, OrderItem

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name','phone' ,'address', 'city', 'postal_code', 'created', 'paid')
    list_filter = ('paid', 'created', 'updated')
    search_fields = ('id', 'first_name', 'last_name', 'email')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'price')
    list_filter = ('order__paid', 'order__created', 'order__updated')
    search_fields = ('order__id', 'product__name')

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
