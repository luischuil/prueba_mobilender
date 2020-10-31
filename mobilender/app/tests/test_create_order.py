# Django
from django.test import TestCase

# Python
import json

# Django Rest Framework
from rest_framework.test import APIClient
from rest_framework import status


class CreateOrderTestCase(TestCase):

    fixtures = ['client.json', 'order.json', 'product.json', 'provider.json']

    def test_create_order_cedis(self):

        client = APIClient()

        test_order = {
            "order_number": "ORD0008",
            "provider": 3,
            "product": 4,
            "client": 1,
            "order_date": "2020-10-30T05:11:30.362Z",
            "priority": True,
            "items": 5,
            "order_type": "CEDIS",
            "distribution_center_store": "Almacén #12"
        }

        response = client.post('/order/', test_order, format='json')
        result = json.loads(response.content)

        response_ok = {
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

        self.assertEqual(result, response_ok)

    def test_create_order_store(self):

        client = APIClient()

        test_order = {
            "order_number": "ORD0007",
            "provider": 1,
            "product": 1,
            "client": 3,
            "order_date": "2020-10-30T05:11:30.362Z",
            "priority": False,
            "items": 2,
            "order_type": "SUCURSAL",
            "store_reference": "Referencia sucursal",
            "store_code": "codigo del almacén"
        }

        response = client.post('/order/', test_order, format='json')
        result = json.loads(response.content)

        response_ok = {
            "order_number": "ORD0007",
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
            "client": 3,
            "client_info":
                {
                    "code": "GJ0001",
                    "name": "Gabriel Juarez",
                    "address": "Calle 22 entre 12 y 23",
                    "client_type": "ORO"
                },
            "order_date": "2020-10-30T05:11:30.362000Z",
            "deliver_date": None,
            "priority": False,
            "items": 2,
            "order_type": "SUCURSAL",
            "distribution_center_store": "",
            "store_reference": "Referencia sucursal",
            "store_code": "codigo del almacén",
            "company_reference": "",
            "company_member_code": "",
            "company_order_detail": ""
        }

        self.assertEqual(result, response_ok)

    def test_create_order_company(self):

        client = APIClient()

        test_order = {
            "order_number": "ORD0006",
            "provider": 2,
            "product": 3,
            "client": 2,
            "order_date": "2020-10-30T05:11:30.362Z",
            "priority": True,
            "items": 6,
            "order_type": "EMPRESA_ASOCIADA",
            "company_reference": "Ref. 12344",
            "company_member_code": "CO3345",
            "company_order_detail": "Descripción orden compañía"
        }

        response = client.post('/order/', test_order, format='json')
        result = json.loads(response.content)

        response_ok = {
            "order_number": "ORD0006",
            "provider": 2,
            "provider_info": {
                "name": "UPS",
                "address": "Calle 11 entre 79-C y 63"
            },
            "product": 3,
            "product_info": {
                "code": "PAN00012",
                "description": "Radio Panasonic RF-2400"
            },
            "client": 2,
            "client_info":
                {
                    "code": "LC0001",
                    "name": "Luis Castro",
                    "address": "Calle 41 entre 77 y 63A",
                    "client_type": "PLATINO"
                },
            "order_date": "2020-10-30T05:11:30.362000Z",
            "deliver_date": None,
            "priority": True,
            "items": 6,
            "order_type": "EMPRESA_ASOCIADA",
            "distribution_center_store": "",
            "store_reference": "",
            "store_code": "",
            "company_reference": "Ref. 12344",
            "company_member_code": "CO3345",
            "company_order_detail": "Descripción orden compañía"
        }

        self.assertEqual(result, response_ok)