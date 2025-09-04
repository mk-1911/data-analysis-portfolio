-- Fuel Efficiency Analysis
-- Question No. 1: 
-- Which manufacturers produce the most fuel-efficient cars?
-- Inputs: cars (columns: make, mpg)
-- Outputs: make, Average_mpg

SELECT make, ROUND(AVG(mpg),2) AS Average_mpg
FROM cars
GROUP BY make
ORDER BY Average_mpg DESC
LIMIT 10;