DELIMITER //
CREATE PROCEDURE my_procedure() BEGIN
SELECT 'Helo from stored procedure';
END //
DELIMITER ;
#RADE POBE VARIJANTE
CALL my_procedure(); 
CALL my_procedure; 
DROP PROCEDURE IF EXISTS my_procedure;
CALL delete_customer_by_id(599);#ne radi iz drugih razloga ali je ok