# BaseDeDatos2024

conda create --name db python=3.11

conda activate db

pip install -r requirements.txt

# Docker Test
docker run hello-world
(Tiene que aparecer:
"Hello from Docker!
This message shows that your installation appears to be working correctly." )

docker run -it python:3.9


cd Clases\01
docker build -t test .
docker run -it test


# Postgres
docker-compose up
(Después de abrir docker desktop y powershell como administrador)

Acceder al docker compose
docker exec -it basededatos2024-db-1 psql -U postgres -d gtfs

Para debuguear si hay algún error
docker logs basededatos2024-db-1