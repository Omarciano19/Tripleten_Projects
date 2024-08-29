-- Crear la tabla temporal y cargar el CSV
CREATE TEMP TABLE temp_csv_data (
    start_ts TIMESTAMP,
    description TEXT,
    duration_seconds INT,
    pickup_location_id INT,
    dropoff_location_id INT
);

COPY temp_csv_data
FROM './datos.csv'
DELIMITER ','
CSV HEADER;

-- Realizar la consulta y exportar los resultados a un nuevo CSV
\COPY (
select company_name, count(trips.trip_id) as trips_amount
from cabs inner join trips on cabs.cab_id=trips.cab_id
where start_ts::date in ('2017-11-15','2017-11-16')

group by cabs.company_name
order by trips_amount  desc


) TO './project_sql_result_01.csv' 
WITH CSV HEADER;