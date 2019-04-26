## Company - Django Rest Framework Project


### API Request Examples

```console
$ curl -X GET localhost:8000/v0/departments/
[{"id":1,"name":"TI"},{"id":2,"name":"Marketing"},{"id":3,"name":"Finance"}]
```

```console
$ curl -H "Content-Type: application/json" -X POST localhost:8000/v0/departments/ -d '{"name" : "Human Resources"}'
{"id":4,"name":"Human Resources"}
```

```console
$ curl -H "Content-Type: application/json" -X PUT localhost:8000/v0/departments/1 -d '{"name" : "IT"}'
{"id":1,"name":"IT"}
```

```console
$ curl -X DELETE localhost:8000/v0/departments/4
```

```console
$ curl -X GET localhost:8000/v0/employees/
[{"id":1,"name":"Claudio","email":"claudio@company.com","department":1},{"id":2,"name":"Marta","email":"marta@company.com","department":2}]
```

```console
$ curl -H "Content-Type: application/json" -X POST localhost:8000/v0/employees/ -d '{"name":"Jose","email":"jose@company.com","department":3}'
{"id":3,"name":"Jose","email":"jose@company.com","department":3}
```

```console
$ curl -H "Content-Type: application/json" -X PATCH localhost:8000/v0/employees/3 -d '{"department" : "1"}'
{"id":3,"name":"Jose","email":"jose@company.com","department":1}
```

```console
$ curl -H "Content-Type: application/json" -X PUT localhost:8000/v0/employees/3 -d '{"name":"Jose Escobar","email":"jose.escobar@company.com","department":1}'
{"id":3,"name":"Jose Escobar","email":"jose.escobar@company.com","department":1}
```

```console
$ curl -X DELETE localhost:8000/v0/employees/3
```