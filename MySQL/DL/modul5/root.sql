CREATE USER 'test_user'@'%' IDENTIFIED BY '12345678';
GRANT SELECT, UPDATE, CREATE, DELETE ON sakila.* TO 'test_user'@'%';
GRANT SELECT, UPDATE, CREATE, DELETE ON *.* TO 'test_user'@'%'; #prava za sve bazepodataka
GRANT ALL PRIVILEGES ON *.* TO 'test_user'@'%'; #dodjeljue sva prava
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'test_user'@'%'; #
DROP USER test_user; #brise