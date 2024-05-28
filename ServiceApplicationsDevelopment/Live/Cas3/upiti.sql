select * from books, authors, book_authors
where books.id = book_authors.book_id
and authors.id = book_authors.author_id
and authors.first_name = 'Marko'

select first_name as ime, last_name as prezime, title as naziv
from books as b join authors as a join book_authors as ba
on b.id = ba.book_id
and a.id = ba.author_id
and first_name='Marko'


#sve ispod je isto, smao sto koristimo pod upite u zavisnosti sta znamo 
# realno znamo samo da se pisac zove marko
select * from books where id in (2,3)

select * from books where id in 
(select book_id from book_authors where author_id=2)

select * from books where id in 
(select book_id from book_authors where author_id= 
(select id from authors where first_name = 'Marko'))

select first_name as ime, last_name as prezime, title as naziv
from books as b join authors as a join book_authors as ba
on b.id = ba.book_id
and a.id = ba.author_id
and title='sql'

