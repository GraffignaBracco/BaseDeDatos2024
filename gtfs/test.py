import dlt
from dlt.sources.filesystem import filesystem, read_csv_duckdb, read_csv
import pandas as pd
from dlt.destinations import postgres

print(help(postgres))

# Definir la connection string de PostgreSQL
connection_string = "postgres://postgres:1234@localhost:5432/gtfs"

# Crear el pipeline con destino PostgreSQL utilizando la connection string
pipeline = dlt.pipeline(
    pipeline_name="static",
    destination=postgres(credentials=connection_string) #"postgres" #dlt.destinations.postgres(connection_string)
)

# Configurar el recurso filesystem para procesar los archivos .txt con DuckDB
# files = os.listdir('Data/feed-gtfs')

for file in ['routes.txt']:
    print(file)
    df = pd.read_csv('../Data/feed-gtfs/agency.txt')
    print(df.head(1))
    # filesystem_pipe = filesystem(
    #     bucket_url="file://home/src/Data/feed-gtfs/",  # Directorio con los archivos
    #     file_glob=file  # Procesar solo archivos .txt
    # ) | read_csv_duckdb()  # Usar DuckDB para procesar los archivos CSV
    
    info = pipeline.run(df, table_name=file.replace('.txt', ''))
    
    print(info)
