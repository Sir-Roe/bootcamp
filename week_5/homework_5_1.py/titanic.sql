--Count how many rows you have.
SELECT COUNT(*) FROM titanic;
--How many people survived?
SELECT COUNT(survived) AS survived FROM titanic WHERE survived != 0;
--What passenger class has the largest population?
SELECT pclass FROM titanic GROUP BY pclass ORDER BY Count(pclass) DESC LIMIT 1