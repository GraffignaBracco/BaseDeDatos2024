\set ON_ERROR_STOP on

COPY agency(agency_id, agency_name, agency_url, agency_timezone, agency_lang, agency_phone)
FROM '../feed-gtfs/agency.txt' DELIMITER ',' CSV HEADER ENCODING 'UTF8';

COPY stops(stop_id, stop_code, stop_name, stop_lat, stop_lon)
FROM '../feed-gtfs/stops.txt' DELIMITER ',' CSV HEADER ENCODING 'UTF8';

COPY routes(route_id, agency_id, route_short_name, route_long_name, route_desc, route_type)
FROM '../feed-gtfs/routes.txt' DELIMITER ',' CSV HEADER ENCODING 'UTF8';

COPY shapes(shape_id, shape_pt_lat, shape_pt_lon, shape_pt_sequence, shape_dist_traveled)
FROM '../feed-gtfs/shapes.txt' DELIMITER ',' CSV HEADER ENCODING 'UTF8';

COPY trips(route_id, service_id, trip_id, trip_headsign, trip_short_name, direction_id, block_id, shape_id, exceptional)
FROM '../feed-gtfs/trips.txt' DELIMITER ',' CSV HEADER ENCODING 'UTF8';

COPY stop_times(trip_id, arrival_time, departure_time, stop_id, stop_sequence, timepoint, shape_dist_traveled)
FROM '../feed-gtfs/stop_times.txt' DELIMITER ',' CSV HEADER ENCODING 'UTF8';

COPY calendar_dates(service_id, date, exception_type)
FROM '../feed-gtfs/calendar_dates.txt' DELIMITER ',' CSV HEADER ENCODING 'UTF8';