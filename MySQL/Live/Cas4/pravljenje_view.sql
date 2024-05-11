CREATE VIEW vFruitInventory AS
SELECT
    Fruit.FruitName,
    Fruit.Inventory,
    Units.UnitName
FROM
Fruit INNER JOIN Units ON
    Fruit.UnitId = Units.UnitId;

SELECT * FROM vFruitInventory;

SELECT FruitName
FROM vFruitInventory
WHERE Inventory <= 10;

SELECT *
FROM Fruit
WHERE FruitId = 1;

/*SELECT *
FROM vFruitInventory
WHERE FruitId = 1;*/ #ne radi

ALTER VIEW vFruitInventory AS
SELECT
Fruit.FruitId,
    Fruit.FruitName,
    Fruit.Inventory,
    Units.UnitName
FROM
Fruit INNER JOIN Units ON
    Fruit.UnitId = Units.UnitId;

SELECT * FROM vFruitInventory;    

CREATE OR REPLACE VIEW vFruitInventory AS
SELECT
    Fruit.FruitName,
    Fruit.Inventory,
    Units.UnitName
FROM
Fruit INNER JOIN Units ON
    Fruit.UnitId = Units.UnitId;
   
CREATE OR REPLACE VIEW vFruitInventory AS
SELECT
Fruit.FruitId,
    Fruit.FruitName,
    Fruit.Inventory,
    Units.UnitName
FROM
Fruit INNER JOIN Units ON
    Fruit.UnitId = Units.UnitId;