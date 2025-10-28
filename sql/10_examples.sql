-- Top call types by confirmation rate
SELECT call_type,
       AVG(confirmed_type IS NOT NULL)::numeric(5,2) AS confirmation_rate
FROM calls c
LEFT JOIN incidents i USING (call_id)
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10;

-- Monthly calls by ZIP
SELECT date_trunc('month', call_datetime) AS month, zip, COUNT(*) AS calls
FROM calls
GROUP BY 1, 2
ORDER BY 1, 3 DESC;
