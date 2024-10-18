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

## 1° Paso: Clonar el repositorio con GIT (Si todavía no lo tenían clonado, si ya lo hicieron en la clase, saltearse esto)

### Abrir VS Code y poner "Clone Git Repository"

![image.png](attachment:image.png)  

### Luego copiar y pegar la URL del repósitorio `https://github.com/GraffignaBracco/BaseDeDatos2024.git` y seleccionar "Clone From URL"

![image-2.png](attachment:image-2.png)

### Seleccionar una carpeta donde se quiera descargar el repositorio


