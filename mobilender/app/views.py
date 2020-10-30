from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework import viewsets
from .filters import OrderFilter
from .models import (Client, Order, Product, Provider)
from .serializers import (ClientSerializer, OrderSerializer, ProductSerializer, ProviderSerializer)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = OrderFilter


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
