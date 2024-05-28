import sqlalchemy as db
from sqlalchemy import text, String, ForeignKey, Table, Column, Integer, ForeignKeyConstraint, select
from sqlalchemy.ext import declarative
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declarative_base, relationship, Session

engine = db.create_engine('mysql+pymysql://root:banjalukA1%@localhost:3306/off')

Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    title = Column(String(30))
    authors = relationship('Author', secondary='book_authors', back_populates='books')


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    first_name = Column(String(30))
    last_name = Column(String(30))
    books = relationship('Book', secondary='book_authors', back_populates='authors')


book_author = Table(
    'book_authors',
    Base.metadata,
    Column('author_id', ForeignKey('authors.id'), primary_key=True),
    Column('book_id', ForeignKey('books.id'), primary_key=True),
    extend_existing=True,
)

Base.metadata.create_all(engine)

with Session(engine) as session:
    post2 = Author(first_name="Katarina", last_name="Caric")
    post3 = Author(first_name="Marko", last_name="Caric")
    session.add_all([post2, post3])

    tag1 = Book(title="python")
    tag2 = Book(title="sql")
    tag3 = Book(title="mysql")
    session.add_all([tag1, tag2, tag3])

    post2.books.append(tag1)
    post2.books.append(tag2)
    post3.books.append(tag2)
    post3.books.append(tag3)

    session.commit()

    stmt = select(Author).where(Author.first_name == "Marko")
    author = session.scalar(stmt)

    for book in author.books:
        print(book.title)

    stmt = select(Book).where(Book.title == "sql")
    book = session.scalar(stmt)

    for author in book.authors:
        print(author.first_name)

