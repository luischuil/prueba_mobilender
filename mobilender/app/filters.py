import django_filters

from .models import Order
from .settings import (CLIENT_TYPES, ORDER_TYPES)


class OrderFilter(django_filters.FilterSet):
    priority = django_filters.BooleanFilter(field_name='priority')
    order_type = django_filters.ChoiceFilter(choices=ORDER_TYPES)
    client_type = django_filters.ChoiceFilter(choices=CLIENT_TYPES, field_name='client__client_type')
    delivered = django_filters.BooleanFilter(method='delivered_filter')

    class Meta:
        model = Order
        fields = [
            'priority',
            'order_type',
            'client_type',
            'delivered',
        ]

    def delivered_filter(self, queryset, name, value):
        return queryset.exclude(deliver_date__isnull=value)
