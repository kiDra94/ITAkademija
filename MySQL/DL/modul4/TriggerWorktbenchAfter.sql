CREATE DEFINER=`root`@`localhost` TRIGGER `customer_AFTER_INSERT` AFTER INSERT ON `customer` FOR EACH ROW BEGIN

INSERT INTO name_backup (name_backup_name) VALUES (new.first_name);

END