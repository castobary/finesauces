from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'first_name', 'last_name',
        'email', 'address', 'postal_code',
        'city', 'transport', 'created',
        'status'
    ]
    list_filter = [
        'created', 'updated'
    ]

    inlines = [OrderItemInline]