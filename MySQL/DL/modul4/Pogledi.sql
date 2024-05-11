SELECT customer.first_name, customer.last_name, address.address, address.district, city.city, country.country
FROM customer JOIN address ON address.address_id = customer.address_id
JOIN city ON city.city_id = address.city_id
JOIN country ON country.country_id = city.country_id;
#nakon kreiranja pogleda
SELECT * FROM customer_details;
CREATE USER John;
GRANT SELECT ON customer_details TO John;