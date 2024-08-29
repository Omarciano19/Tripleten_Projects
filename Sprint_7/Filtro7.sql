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
    SELECT start_ts, 
        CASE 
            WHEN description LIKE '%rain%' OR description LIKE '%storm%' THEN 'Bad'
            ELSE 'Good' 
        END AS weather_conditions,
        duration_seconds
    FROM temp_csv_data
    WHERE pickup_location_id = 50 
      AND dropoff_location_id = 63 
      AND EXTRACT(DOW FROM start_ts) = 6
    ORDER BY start_ts
) TO './project_sql_result_07.csv' 
WITH CSV HEADER;
