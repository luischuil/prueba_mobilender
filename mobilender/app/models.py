from django.db import models
from .settings import (CLIENT_TYPES, ORDER_TYPES)


class Client(models.Model):
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=70)
    image_url = models.URLField(blank=True)
    address = models.CharField(max_length=100)
    client_type = models.CharField(max_length=10, choices=CLIENT_TYPES)


class Order(models.Model):
    order_number = models.CharField(max_length=30)
    provider = models.ForeignKey('app.Provider', related_name='orders', on_delete=models.CASCADE)
    product = models.ForeignKey('app.Product', related_name='orders', on_delete=models.CASCADE)
    client = models.ForeignKey('app.Client', related_name='orders', on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    deliver_date = models.DateTimeField()
    priority = models.BooleanField(default=False)
    items = models.IntegerField(default=0)
    order_type = models.CharField(max_length=20, choices=ORDER_TYPES)
    distribution_center_store = models.CharField(max_length=50, blank=True)
    store_reference = models.CharField(max_length=100, blank=True)
    store_code = models.CharField(max_length=30, blank=True)
    company_reference = models.CharField(max_length=100, blank=True)
    company_member_code = models.CharField(max_length=30, blank=True)
    company_order_detail = models.TextField(blank=True)


class Product(models.Model):
    code = models.CharField(max_length=30)
    description = models.TextField()


class Provider(models.Model):
    name = models.CharField(max_length=70)
    address = models.CharField(max_length=100)


class ProviderProduct(models.Model):
    provider = models.ForeignKey('app.Provider', related_name='provider_products', on_delete=models.CASCADE)
    product = models.ForeignKey('app.Product', related_name='provider_products', on_delete=models.CASCADE)
