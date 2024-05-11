CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `customer_details` AS
    SELECT 
        `customer`.`first_name` AS `first_name`,
        `customer`.`last_name` AS `last_name`,
        `address`.`address` AS `address`,
        `address`.`district` AS `district`,
        `city`.`city` AS `city`,
        `country`.`country` AS `country`
    FROM
        (((`customer`
        JOIN `address` ON ((`address`.`address_id` = `customer`.`address_id`)))
        JOIN `city` ON ((`city`.`city_id` = `address`.`city_id`)))
        JOIN `country` ON ((`country`.`country_id` = `city`.`country_id`)))