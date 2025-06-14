
# Melania API

Una API sencilla con FastAPI para Melania Bot. Lista para deploy en Railway o VPS con Docker.

## Comandos

### Build local
docker build -t melania-api .

### Correr local
docker run -d -p 8000:80 melania-api

### Testear en browser/Postman
http://localhost:8000/
