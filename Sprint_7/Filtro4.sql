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
select neighborhood_id, name from neighborhoods 
    where name in ('O''Hare','Loop');

) TO './project_sql_result_04.csv' 
WITH CSV HEADER;