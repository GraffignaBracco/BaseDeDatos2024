import io
import pandas as pd
import requests
import aiohttp
import asyncio
import nest_asyncio

from google.transit import gtfs_realtime_pb2

nest_asyncio.apply()  # Aplica parche para permitir bucles anidados

import logging

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
async def fetch_feed(session, url, params):
    try:
        async with session.get(url, params=params) as response:
            response.raise_for_status()  # Levantará una excepción para respuestas de error HTTP
            content = await response.read()
            feed = gtfs_realtime_pb2.FeedMessage()
            feed.ParseFromString(content)
            return feed
    except aiohttp.ClientError as e:
        logging.error(f"Error de cliente HTTP: {e}")
        print(e)
    except Exception as e:
        print(e)
        logging.error(f"Error inesperado: {e}")
    return None

async def main(client_id, client_secret):
    params = {
        'client_id': client_id,
        'client_secret': client_secret
    }
    url_positions = "https://apitransporte.buenosaires.gob.ar/colectivos/vehiclePositions"
    url_trip_updates = "https://apitransporte.buenosaires.gob.ar/colectivos/tripUpdates"

    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch_feed(session, url_positions, params),
            fetch_feed(session, url_trip_updates, params)
        ]
        feed_vehpo, feed_tripup = await asyncio.gather(*tasks)

        if feed_vehpo and feed_tripup:
            # Procesamiento de datos aquí
            pass
    return feed_vehpo, feed_tripup


if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

def extract_trip_updates(feed):
    """
    Extrae los datos de trip updates de un objeto FeedMessage GTFS Realtime
    y los convierte en un DataFrame de pandas.
    
    Parámetros:
    - feed: Una instancia de gtfs_realtime_pb2.FeedMessage que contiene los trip updates.
    
    Retorna:
    - Un DataFrame de pandas con los datos de trip updates.
    """
    data = []
    for entity in feed.entity:
        if entity.HasField('trip_update'):
            trip_update = entity.trip_update
            trip = trip_update.trip
            vehicle = trip_update.vehicle

            for stop_time_update in trip_update.stop_time_update:
                arrival = stop_time_update.arrival
                data.append({
                    "header_timestamp" : feed.header.timestamp,
                    "entity_id": entity.id,
                    "trip_id": trip.trip_id,
                    "route_id": trip.route_id,
                    "start_time": trip.start_time,
                    "start_date": trip.start_date,
                    "vehicle_id": vehicle.id,
                    "vehicle_label": vehicle.label,
                    "stop_sequence": stop_time_update.stop_sequence,
                    "stop_id": stop_time_update.stop_id,
                    "arrival_delay": arrival.delay if arrival.HasField('delay') else None,
                    "arrival_time": arrival.time if arrival.HasField('time') else None
                })

    # Convertir a DataFrame
    df = pd.DataFrame(data)
    return df

def extract_vehicle_positions(feed):
    """
    Extrae los datos de las posiciones de los vehículos de un objeto FeedMessage GTFS Realtime
    y los convierte en un DataFrame de pandas.
    
    Parámetros:
    - feed: Una instancia de gtfs_realtime_pb2.FeedMessage que contiene las posiciones de los vehículos.
    
    Retorna:
    - Un DataFrame de pandas con los datos de las posiciones de los vehículos.
    """
    data = []
    for entity in feed.entity:
        if entity.HasField('vehicle'):
            vehicle = entity.vehicle
            position = vehicle.position
            trip = vehicle.trip
            data.append({
                "header_timestamp" : feed.header.timestamp,
                "entity_id": entity.id,
                "vehicle_id": vehicle.vehicle.id,
                "vehicle_label": vehicle.vehicle.label,
                "current_stop_sequence": vehicle.current_stop_sequence,
                "stop_id": vehicle.stop_id,
                "latitude": position.latitude,
                "longitude": position.longitude,
                "odometer": position.odometer if position.HasField('odometer') else None,
                "speed": position.speed if position.HasField('speed') else None,
                "timestamp": vehicle.timestamp,
                "trip_id": trip.trip_id if trip.HasField('trip_id') else None,
                "route_id": trip.route_id if trip.HasField('route_id') else None,
                "start_time": trip.start_time if trip.HasField('start_time') else None,
                "start_date": trip.start_date if trip.HasField('start_date') else None
            })

    # Convertir a DataFrame
    df = pd.DataFrame(data)
    return df

@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    client_id = '46ca3fbfd5984ba8aa6a39cc165e43d1'
    client_secret = '621C7e8e3bdf41bC99095408AD1878F4'
    vehpo, tripup = asyncio.run(main(client_id, client_secret))

    
    return extract_vehicle_positions(vehpo), extract_trip_updates(tripup)  #pd.read_csv(io.StringIO(response.text), sep=',')

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
