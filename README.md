# API de Lista de Tareas

Esta es una API RESTful creada con Python y FastAPO para manejar una lista de tareas.

## Requisitos

- Python 3.10+
- Docker

## Variables de Entorno
Primero se debe configurar las variables de entorno necesarias para levantar el proyecto localmente, las cuales son las que se muestran en el `.env.sample` y a continuación:

```bash
POSTGRES_DB=database_name
POSTGRES_USER=database_user
POSTGRES_PASSWORD=database_password
POSTGRES_HOST=database_host
```

## Levantar la Aplicación
Para ejecutar la aplicación en Docker:
```bash
docker compose up --build -d
```

También puedes ver los logs de la app ejecutando el siguiente comando:

```bash
docker compose logs -f app
```

## Pruebas
Para ejecutar las pruebas:
```bash
docker compose exec app pytest --cov=. tests/
```

## Documentacion
Para encontrar la documentación solo debes acceder al [swagger](http://localhost:8000/docs).
