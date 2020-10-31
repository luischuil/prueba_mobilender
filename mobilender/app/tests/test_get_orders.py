# Django
from django.test import TestCase

# Python
import json

# Django Rest Framework
from rest_framework.test import APIClient
from rest_framework import status


class GetOrdersTestCase(TestCase):

    fixtures = ['client.json', 'order.json', 'product.json', 'provider.json']

    def test_get_orders(self):

        client = APIClient()

        response = client.get(
            '/order/?priority=true&order_type=CEDIS&client_type=PLATINO&delivered=false', format='json'
        )
        result = json.loads(response.content)

        response_ok = [
            {
                "order_number": "ORD0001",
                "provider": 1,
                "provider_info": {
                    "name": "Estafeta",
                    "address": "Calle 12 entre 88 y 13A"
                },
                "product": 1,
                "product_info": {
                    "code": "SN03345",
                    "description": "Sony MDREX14APB Audífonos intrauditivos"
                },
                "client": 1,
                "client_info":
                    {
                        "code": "AV0001",
                        "name": "Ana Velazquez",
                        "address": "Calle 23 entre 45 y 23",
                        "client_type": "PLATINO"
                    },
                "order_date": "2020-10-30T05:11:30.362000Z",
                "deliver_date": None,
                "priority": True,
                "items": 1,
                "order_type": "CEDIS",
                "distribution_center_store": "Almacén A",
                "store_reference": "",
                "store_code": "",
                "company_reference": "",
                "company_member_code": "",
                "company_order_detail": ""
            }, {
                "order_number": "ORD0008",
                "provider": 3,
                "provider_info": {
                    "name": "Fedex",
                    "address": "Calle 51 entre 91 y 22A"
                },
                "product": 4,
                "product_info": {
                    "code": "DUR22290",
                    "description": "Pilas Duracell Copper negro"
                },
                "client": 1,
                "client_info":
                    {
                        "code": "AV0001",
                        "name": "Ana Velazquez",
                        "address": "Calle 23 entre 45 y 23",
                        "client_type": "PLATINO"
                    },
                "order_date": "2020-10-30T05:11:30.362000Z",
                "deliver_date": None,
                "priority": True,
                "items": 5,
                "order_type": "CEDIS",
                "distribution_center_store": "Almacén #12",
                "store_reference": "",
                "store_code": "",
                "company_reference": "",
                "company_member_code": "",
                "company_order_detail": ""
            }
        ]

        self.assertEqual(result, response_ok)
