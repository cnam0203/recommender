from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, unique=True)
    price = models.IntegerField(blank=True, null=True)

class Transaction(models.Model):
    product_id = models.ForeignKey(Product, blank=False, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
