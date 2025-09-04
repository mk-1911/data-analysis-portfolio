-- Fuel Type Insights
-- Question No. 5
-- Which Fuel type is most efficient on average and most common?
-- Inputs: cars (columns: fuel_type, mpg)
-- Outputs: fuel_type, count, Average_mpg

SELECT fuel_type, COUNT(*) AS count, ROUND(AVG(mpg),2) AS Average_mpg
FROM cars
GROUP BY fuel_type
ORDER BY Average_mpg DESC;