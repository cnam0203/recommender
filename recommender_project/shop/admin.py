from django.contrib import admin
from .models import Product, Transaction

# Register your models here.
class Product_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')

# admin.site.register(Product)
admin.site.register(Product, Product_Admin)
admin.site.register(Transaction)