## API

### GET /deposit

Возвращает расчёт депозита.

Пример запроса:

```http
GET /deposit HTTP/1.1
Host: example.com
Content-Type: application/json

{
    "date": "01.01.2022",
    "periods": 1,
    "amount": 10000,
    "rate": 2
}
```

## DOCKER

### Аргументы

* `HOST`: адрес хоста
* `PORT`: порт

Пример использования:

```bash
docker run -d \
  -e HOST=localhost \
  -e PORT=8080 \
  my-image
```

[![codecov](https://codecov.io/gh/Ar-b-ra/REST_Test/branch/master/graph/badge.svg)](https://codecov.io/gh/Ar-b-ra/REST_Test)