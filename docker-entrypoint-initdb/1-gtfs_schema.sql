{# CREATE TABLE agency (
    agency_id TEXT, -- PRIMARY KEY,
    agency_name TEXT,
    agency_url TEXT,
    agency_timezone TEXT,
    agency_lang TEXT,
    agency_phone TEXT
);

CREATE TABLE calendar_dates (
    service_id INT, -- PRIMARY KEY,
    date DATE,
    exception_type INT
);

CREATE TABLE routes (
    route_id TEXT, -- PRIMARY KEY,
    agency_id TEXT,
    route_short_name TEXT,
    route_long_name TEXT,
    route_desc TEXT,
    route_type INT --,
    --FOREIGN KEY (agency_id) REFERENCES agency(agency_id)
);

CREATE TABLE shapes (
    shape_id TEXT,
    shape_pt_lat NUMERIC,
    shape_pt_lon NUMERIC,
    shape_pt_sequence INT,
    shape_dist_traveled NUMERIC --,
    --PRIMARY KEY (shape_id, shape_pt_sequence)

);


CREATE TABLE stops (
    stop_id TEXT, -- PRIMARY KEY,
    stop_code TEXT,
    stop_name TEXT,
    stop_lat NUMERIC,
    stop_lon NUMERIC
);

CREATE TABLE stop_times (
    trip_id TEXT,
    arrival_time TEXT,
    departure_time TEXT,
    stop_id TEXT,
    stop_sequence INT,
    timepoint INT,
    shape_dist_traveled NUMERIC --,
    --PRIMARY KEY (trip_id, stop_sequence)
);


CREATE TABLE trips (
    route_id TEXT,
    service_id TEXT,
    trip_id TEXT, -- PRIMARY KEY,
    trip_headsign TEXT,
    trip_short_name TEXT,
    direction_id INT,
    block_id TEXT,
    shape_id TEXT,
    exceptional INT --,
    --FOREIGN KEY (route_id) REFERENCES routes(route_id) -- Referencia compuesta
); #}
