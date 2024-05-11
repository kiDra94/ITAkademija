from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///assigment.db', echo = True)
#echo prikazuje u terminalu sql kode
meta = MetaData()

books = Table(
    'students', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', String),
    Column('year', String),
)
meta.create_all(engine) 
conn = engine.connect()
result = conn.execute(books.insert(), [
   {'title':'Dnevnik o Carnojevicu', 'year' : '1921'},
   {'title':'Seobe','year' : '1929'},
   {'title':'Druga knjiga Seoba','year' : '1962'},
   {'title':'Roman o Londonu','year' : '1971'},
])
# conn.commit()
citanje = conn.execute(books.select())
for i in citanje:
    print(i)
conn.commit()
conn.close()
