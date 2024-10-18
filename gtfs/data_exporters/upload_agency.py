import dlt 
import os
from dotenv import load_dotenv

# Cargar las variables desde el archivo .env
load_dotenv(dotenv_path='.env')

# Función para crear la connection string a partir de las variables del .env
def create_connection_string():
    user = os.getenv('POSTGRES_USER')
    password = os.getenv('POSTGRES_PASSWORD')
    host = os.getenv('POSTGRES_HOST')
    port = os.getenv('POSTGRES_PORT')
    dbname = os.getenv('POSTGRES_DBNAME')
    # Construir la connection string
    connection_string = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
    return connection_string


# Imprimir la connection string


if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

from dlt.sources.filesystem import filesystem, read_csv_duckdb, read_csv


@data_exporter
def export_data(*args, **kwargs):
    """
    Exports data to some source.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Output (optional):
        Optionally return any object and it'll be logged and
        displayed when inspecting the block run.
    """
    # Specify your data exporting logic here

    # Generar la connection string
    # connection_string = create_connection_string()


    # Configuración del pipeline para leer archivos CSV
    # filesystem_pipe = filesystem(
    #     bucket_url="Data/feed-gtfs",  # Ruta al sistema de archivos
    #     file_glob="*.txt"  # Filtrar por archivos CSV
    # ) | read_csv()
    # # Crear el pipeline de DLT utilizando la connection string
    # pipeline = dlt.pipeline(
    #     pipeline_name="gtfs_static",
    #     destination=dlt.destinations.postgres(connection_string),
    #     dataset_name="gtfs_static"
    # )

    import dlt
    from dlt.sources.filesystem import filesystem, read_csv_duckdb

    # Definir la connection string de PostgreSQL
    connection_string = "postgresql://postgres:1234@db:5432/gtfs"

    # Crear el pipeline con destino PostgreSQL utilizando la connection string
    pipeline = dlt.pipeline(
        pipeline_name="static",
        destination=dlt.destinations.postgres(connection_string)
    )

    # Configurar el recurso filesystem para procesar los archivos .txt con DuckDB
    files = os.listdir('Data/feed-gtfs')
    
    for file in ['routes.txt']:
        print(file)
        if files == 'stop_times.txt':
            next

        filesystem_pipe = filesystem(
            bucket_url="file://home/src/Data/feed-gtfs/",  # Directorio con los archivos
            file_glob=file  # Procesar solo archivos .txt
        ) | read_csv()  # Usar DuckDB para procesar los archivos CSV
        
        info = pipeline.run(filesystem_pipe, table_name=file.replace('.txt', ''))
        
        print(info)





    # Ejecutar el pipeline para cargar cada archivo en una tabla
    # for file_item in filesystem_pipe:
    #     print(f"Procesando archivo: {file_item.path.name}")  # Verifica el archivo leído
    #     table_name = file_item.path.stem  # El nombre del archivo se convierte en el nombre de la tabla
    #     pipeline.run(file_item, table_name=table_name)
    #     print(f"Archivo {file_item.path.name} cargado en la tabla {table_name}")

