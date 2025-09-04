-- Cylinders vs Fuel Efficiency
-- Question No. 3
-- How does the number of cylinders affect MPG?
-- Inputs: cars (columns: cylinders, mpg)
-- Outputs: cylinders, Average_mpg

SELECT cylinders, AVG(mpg) AS Average_mpg
FROM cars
GROUP BY cylinders
ORDER BY Average_mpg DESC;