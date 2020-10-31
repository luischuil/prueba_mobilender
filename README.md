# Prueba Mobileder
Prueba de programación
## Requerimientos
Para probar la api se requiere tener instalado docker y docker compose.

## Instalación
```python
#Clonar el repositorio.
$ git clone git@github.com:luischuil/prueba_mobilender.git

#En la carpeta raiz del proyecto ejecutar el siguiente comando para iniciar la api.
$ sudo docker-compose up
```
El sitio estará disponible en la siguiente dirección:
[http://localhost:8000/](http://localhost:8000/)

## Diagrama BD
El diagrama de BD se encuentra disponible [Aquí](https://github.com/luischuil/prueba_mobilender/blob/main/images/diagrama%20bd%20mobilender.png) 

## Endpoint para agregar un pedido
POST [http://localhost:8000/order/](http://localhost:8000/order/) 

Los parámetros que recibe el endpoint será en formato json

** Ejemplo body para agregar pedido hacia el centro de distribución:** 
```
{
	"order_number": "ORD0008",                    // número de orden
	"provider": 3,                                // id del proveedor
	"product": 4,                                 // id del producto
	"client": 1,                                  // id del cliente
	"order_date": "2020-10-30T05:11:30.362Z",     // fecha de la orden
	"priority": true,                             // prioridad
	"items": 5,                                   // cantidad solicitada
	"order_type": "CEDIS",                        // tipo de orden
	"distribution_center_store": "Almacén #12",   // referencia sucursal
}
```

** Ejemplo body para agregar pedido hacia una sucursal:** 
```
{
	"order_number": "ORD0007",                  // número de orden
	"provider": 1,                              // id del proveedor
	"product": 1,                               // id del producto
	"client": 3,                                // id del cliente
	"order_date": "2020-10-30T05:11:30.362Z",   // fecha de la orden
	"priority": false,                          // prioridad
	"items": 2,                                 // cantidad solicitada
	"order_type": "SUCURSAL",                   // tipo de orden
	"store_reference": "Referencia sucursal",   // referencia sucursal
	"store_code": "codigo del almacén"          // código de la sucursal
}
```

** Ejemplo body para agregar pedido hacia una empresa asociada:** 
```
{
	"order_number": "ORD0006",                            // número de orden
	"provider": 2,                                        // id del proveedor
	"product": 3,                                         // id del producto
	"client": 2,                                          // id del cliente
	"order_date": "2020-10-30T05:11:30.362Z",             // fecha de la orden
	"priority": true,                                     // prioridad
	"items": 6,                                           // cantidad solicitada
	"order_type": "EMPRESA_ASOCIADA",                     // tipo de orden
	"company_reference": "Ref. 12344",                    // referencia empresa asociada
	"company_member_code": "CO3345",                      // código empresa asociada
	"company_order_detail": "Descripción orden compañía"  // detalle del pedido
}
```
## Endpoint para consultar pedidos
GET [http://localhost:8000/order/?priority=true&order_type=CEDIS&client_type=PLATINO&delivered=false](http://localhost:8000/order/?priority=true&order_type=CEDIS&client_type=PLATINO&delivered=false) 

El resultado tendrá el siguiente formato:
```
[
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
    "client_info": {
      "code": "AV0001",
      "name": "Ana Velazquez",
      "address": "Calle 23 entre 45 y 23",
      "client_type": "PLATINO"
    },
    "order_date": "2020-10-30T05:11:30.362000Z",
    "deliver_date": null,
    "priority": true,
    "items": 1,
    "order_type": "CEDIS",
    "distribution_center_store": "Almacén A",
    "store_reference": "",
    "store_code": "",
    "company_reference": "",
    "company_member_code": "",
    "company_order_detail": ""
  },
  {
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
    "client_info": {
      "code": "AV0001",
      "name": "Ana Velazquez",
      "address": "Calle 23 entre 45 y 23",
      "client_type": "PLATINO"
    },
    "order_date": "2020-10-30T05:11:30.362000Z",
    "deliver_date": null,
    "priority": true,
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
```

## Unit test
```python
#con el proyecto iniciado, ejecute
$ docker ps

#copie el valor del CONTAINER ID correspondiente a la imagen a continuación
CONTAINER ID     IMAGE                                    COMMAND
a1ads6dt34ad     prueba_mobilender_mobilender_django      "bash -c 'python man…"

#Sustituya el valor en lugar de <container-id>, este comando ejecutara las pruebas
$ docker exec -it <container-id> python /code/manage.py test app.tests
```