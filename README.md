# BaseDeDatos2024

## Estructura del Repositorio

BaseDeDatos2024  
├── Clases  
│   ├── 00_Introducción  
│   ├── 01_Bases_De_Datos  
│   ├── 02_Orquestacion  
│   ├── 03_SQL  
│   ├── 04_DataWarehouses  
│   ├── 04_NocoDB  
├── docker-entrypoint-initdb  
├── gtfs  
│   ├── .ssh_tunnel  
│   ├── charts  
│   ├── custom  
│   ├── custom_templates  
│   │   ├── blocks  
│   │   │   ├── dlt_ingestion  
│   ├── data_exporters  
│   ├── data_loaders  
│   ├── dbt  
│   ├── extensions  
│   ├── interactions  
│   ├── pipelines  
│   │   ├── bitter_arcanist  
│   │   ├── endearing_pine  
│   │   ├── example_pipeline  
│   │   ├── gtfs_realtime_pipeline  
│   │   ├── gtfs_static_pipeline  
│   │   ├── gtfs_static_pipeline_dlt  
│   │   ├── test  
│   │   ├── yrdy  
│   ├── scratchpads  
│   ├── transformers  
│   ├── utils  
├── mage_data  
│   ├── gtfs  
│   │   ├── .operation_history  
│   │   ├── pipelines  
│   │   │   ├── gtfs_realtime_pipeline  
│   │   │   ├── gtfs_static_pipeline  
│   │   ├── test  
├── .env.example  
├── Dockerfile  
├── README.md  
├── docker-compose.yml  
├── poetry.lock  
├── pyproject.toml  
├── requirements.txt  

## 1° Paso: Clonar el repositorio
 Ir al Repositorio de GitHub:
 
 ![alt text](image.png)

Ir a "Branch"

![alt text](image-1.png)

Crear una nueva Branch con su nombre

![alt text](image-2.png)


![alt text](image-3.png)

Clonar el repositorio con

```bash
git clone https://github.com/GraffignaBracco/BaseDeDatos2024.git
```

Cambiar a la branch que crearon:

![alt text](image-5.png)


## 2° Paso: Crear un Ambiente de python para poder usar las librerías necesarias.


Lo primero que hay que hacer es "ir" con la terminal hasta la carpeta del Repositorio. Esto se hace con este comando desde la misma terminal de VSCode:

```bash
cd BaseDeDatos2024
```

### Opción 1: Con Anaconda

Una vez que estamos en la carpeta del repositorio  utiliza el siguiente comando para crear un entorno llamado `base_de_datos` con Python 3.11:
```bash
conda create --name base_de_datos python=3.11
```
Una vez creado, activa el entorno con el siguiente comando:

```bash
conda activate base_de_datos
```

Luego, instalá las dependencias con este comando:

```bash
pip install -r requirements.txt
```

### Opción 2: Con Poetry
Si no quieren usar anaconda, pueden usar poetry que es otra librería para manejar dependencias

el primer paso es instalar la librería

```bash
pip install poetry
```

Luego, instalan todas las dependencias con el comando:

```bash
poetry install
```

Una vez que las dependencias estén instaladas, puedes acceder al entorno virtual de Poetry con:

```bash
poetry shell
```

Para crear un kernel en Jupyter vinculado a este entorno de Poetry, ejecuta el siguiente comando:

```bash
python -m ipykernel install --user --name=base_de_datos --display-name "Python (base_de_datos)"
```



Luego abrir el jupyter notebook `Ejercicio_Clase1.ipynb` y poner "Seleccionar Kernel" En la parte superior Derecha.

![image-2.png](attachment:image-2.png)

Luego seleccionar el kernel creado 

![image.png](attachment:image.png)

A veces el Kernel demora en aparecer en esta lista de opciones. Por ahí funciona reiniciar VS Code y volver a probar


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



