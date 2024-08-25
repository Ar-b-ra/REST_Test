## Основная форма

Для того, чтобы увидеть расчёт депозита, достаточно запустить приложение и перейти по ссылке: `<HOST>:<PORT>>`

## API

### GET /deposit

Возвращает расчёт депозита.

Пример запроса:

```http
"GET /deposit?date=21.01.2024&periods=7&amount=10000&rate=2 HTTP/1.1"
Content-Type: application/json
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