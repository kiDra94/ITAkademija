CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_customer_by_id`(customerID int)
BEGIN
DELETE FROM customer WHERE customer_id = customerID;
END