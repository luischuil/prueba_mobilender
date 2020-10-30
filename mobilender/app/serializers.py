from rest_framework import serializers
from .models import (Client, Order, Product, Provider)


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            'code',
            'name',
            'address',
            'client_type',
        )


class OrderSerializer(serializers.ModelSerializer):
    provider_info = serializers.SerializerMethodField()
    product_info = serializers.SerializerMethodField()
    client_info = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = (
            'order_number',
            'provider',
            'provider_info',
            'product',
            'product_info',
            'client',
            'client_info',
            'order_date',
            'deliver_date',
            'priority',
            'items',
            'order_type',
            'distribution_center_store',
            'store_reference',
            'store_code',
            'company_reference',
            'company_member_code',
            'company_order_detail',
        )

    def get_provider_info(self, obj):
        return ProviderSerializer(obj.provider).data

    def get_product_info(self, obj):
        return ProductSerializer(obj.product).data

    def get_client_info(self, obj):
        return ClientSerializer(obj.client).data

    def validate(self, data):

        if data['order_type'] == 'CEDIS':

            if not data['distribution_center_store']:
                raise serializers.ValidationError("Field distribution_center_store is required.")

        if data['order_type'] == 'SUCURSAL':

            if not data['store_reference']:
                raise serializers.ValidationError("Field store_reference is required.")

            if not data['store_code']:
                raise serializers.ValidationError("Field store_code is required.")

        if data['order_type'] == 'EMPRESA_ASOCIADA':

            if not data['company_reference']:
                raise serializers.ValidationError("Field company_reference is required.")

            if not data['company_member_code']:
                raise serializers.ValidationError("Field company_member_code is required.")

            if not data['company_order_detail']:
                raise serializers.ValidationError("Field company_order_detail is required.")

        return data


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'code',
            'description',
        )


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = (
            'name',
            'address',
        )
