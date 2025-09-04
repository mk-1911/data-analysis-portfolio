-- Top Efficiency by Engine Type and Horsepower
-- Question No. 7
-- How does engine configuration affect fuel efficiency at different horsepower levels?
-- Can we identify which engine types deliver the best MPG for their power class?
-- Inputs: cars (columns: cylinders, horsepower (arranged into bins), mpg, engine_size)
-- Output: cylinders, avg_mpg, avg_engine_size
-- Notes: cylinders and engine_size were previously engine_type, but it has been split into cylinders and engine_size

SELECT
	cylinders,
	CASE
		WHEN horsepower <= 150 THEN '0-150'
        WHEN horsepower <= 200 THEN '151-200'
        WHEN horsepower <= 250 THEN '201-250'
        ELSE '250+'
	END AS hp_range,
    ROUND(AVG(mpg),2) AS avg_mpg,
    ROUND(AVG(engine_size),2) AS avg_engine_size,
    COUNT(*) AS count
FROM cars
GROUP BY cylinders, hp_range
ORDER BY cylinders, hp_range;
