import sqlalchemy as db
from sqlalchemy import text, String, ForeignKey, Table, Column, Integer, ForeignKeyConstraint, select
from sqlalchemy.ext import declarative
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declarative_base, relationship, Session

engine = db.create_engine('mysql+pymysql://root:banjalukA1%@localhost:3306/off')


def TableArgsMeta(table_args):
    class _TableArgsMeta(declarative.DeclarativeMeta):

        def __init__(cls, name, bases, dict_):
            if (  # Do not extend base class
                    '_decl_class_registry' not in cls.__dict__ and
                    # Missing __tablename_ or equal to None means single table
                    # inheritance — no table for it (columns go to table of
                    # base class)
                    cls.__dict__.get('__tablename__') and
                    # Abstract class — no table for it (columns go to table[s]
                    # of subclass[es]
                    not cls.__dict__.get('__abstract__', False)):
                ta = getattr(cls, '__table_args__', {})
                if isinstance(ta, dict):
                    ta = dict(table_args, **ta)
                    cls.__table_args__ = ta
                else:
                    assert isinstance(ta, tuple)
                    if ta and isinstance(ta[-1], dict):
                        tad = dict(table_args, **ta[-1])
                        ta = ta[:-1]
                    else:
                        tad = dict(table_args)
                    cls.__table_args__ = ta + (tad,)
            super(_TableArgsMeta, cls).__init__(name, bases, dict_)

    return _TableArgsMeta


Base = declarative_base(
    name='Base',
    metaclass=TableArgsMeta({'mysql_engine': 'InnoDB'}))


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
    mysql_engine = 'InnoDB',
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

