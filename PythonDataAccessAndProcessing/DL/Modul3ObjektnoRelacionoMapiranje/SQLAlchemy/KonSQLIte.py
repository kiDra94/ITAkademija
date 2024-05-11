from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///example.db', echo = True)
#echo prikazuje u terminalu sql kode
meta = MetaData()

students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('address', String),
)

meta.create_all(engine) 
'''query = students.insert().values(id = 100,
                                 name = 'Bob Johnson', 
                                 address = 'Green avenue 2331')'''
# query = students.select()
# query = students.update().where(students.c.id == '100').values(name = 'Floorstreet 5')
query = students.delete().where(students.c.id == '100')
conn = engine.connect()
result = conn.execute(query)
conn.commit()
conn.close()