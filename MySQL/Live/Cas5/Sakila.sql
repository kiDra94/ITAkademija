SELECT category.name, AVG(length) FROM  film JOIN film_category USING (film_id) JOIN category USING (category_id)
GROUP BY category.name ORDER BY AVG(length) DESC;
