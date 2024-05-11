CREATE DEFINER=`root`@`localhost` TRIGGER `customer_BEFORE_UPDATE` BEFORE UPDATE ON `customer` FOR EACH ROW BEGIN

IF length(new.first_name) < 4 THEN
SET new.first_name = md5(new.first_name);
END IF;
END