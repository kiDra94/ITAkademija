DELIMITER //

CREATE PROCEDURE spCheckFruitStock(thisFruit SMALLINT)
BEGIN
SELECT
Fruit.FruitName,
Fruit.Inventory,
Units.UnitName
FROM
Fruit INNER JOIN Units ON
Fruit.UnitId = Units.UnitId
WHERE
Fruit.FruitId = thisFruit;
END //

CALL spCheckFruitStock(1);

DELIMITER ;

DROP PROCEDURE IF EXISTS spCheckFruitStock; #drop brise

DELIMITER //

CREATE PROCEDURE spCheckFruitStock(thisFruit SMALLINT)
BEGIN
SELECT
Fruit.FruitId,
Fruit.FruitName,
Fruit.Inventory,
Units.UnitName
FROM
Fruit INNER JOIN Units ON
Fruit.UnitId = Units.UnitId
WHERE
Fruit.FruitId = thisFruit;
END //

DELIMITER ;

DROP PROCEDURE IF EXISTS spCheckFruitStockLevel;

DELIMITER //

CREATE PROCEDURE spCheckFruitStockLevel(
IN pFruitId SMALLINT(5),
    OUT pStockLevel VARCHAR(6))
BEGIN
DECLARE stockNumber SMALLINT;
   
SELECT
Fruit.Inventory into stockNumber
FROM
Fruit INNER JOIN Units ON
Fruit.UnitId = Units.UnitId
WHERE
Fruit.FruitId = pFruitId;
       
IF stockNumber > 10 THEN
SET pStockLevel = 'High';
    ELSEIF (stockNumber <= 10 AND stockNumber >= 5) THEN
SET pStockLevel = 'Medium';
    ELSEIF (stockNumber < 5) THEN
SET pStockLevel = 'Low - Please Replace Now!';
END IF;
   
END //

DELIMITER ;

CALL spCheckFruitStockLevel(1, @stockLevel);
select @stockLevel;