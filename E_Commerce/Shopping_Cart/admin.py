from django.contrib import admin

from Shopping_Cart.models import Product
from Shopping_Cart.models import Customer


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "stock",
        "customer",
    )
    search_fields = ("name", "customer", "stock")
    list_filter = ("name", "customer", "availability")
    ordering = ("name",)


class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name"
    )
    list_filter = ("id", "name")
    search_fields = ("id", "name")
    ordering = ("id", "name")


admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
