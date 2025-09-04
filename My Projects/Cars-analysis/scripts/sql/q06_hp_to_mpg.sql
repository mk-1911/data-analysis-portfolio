-- Top Performance Cars by Efficiency
-- Question No. 6
-- Which Top 10 Cars has the best horsepower-to-MPG ratio?
-- Inputs: cars (columns: make, model_year, horsepower, mpg)
-- Outputs: make, model_year, horsepower, mpg, hp_to_mpg_ratio

SELECT make, model_year, horsepower, mpg, ROUND((horsepower/mpg),2) AS hp_to_mpg_ratio
FROM cars
ORDER BY hp_to_mpg_ratio DESC
LIMIT 10;