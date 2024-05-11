from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
 
engine = create_engine('sqlite:///assigment.db', echo = True)

meta = MetaData()

fruits = Table(
   'Fruit', meta, 
   Column('id', String, primary_key = True), 
   Column('name', String),
   Column('price_per_kg', Integer)
)
 
meta.create_all(engine)
 
query1 = fruits.insert().values(id = '99', 
                                  name = 'banana',
                                     price_per_kg=50)
 
conn = engine.connect()
 
conn.execute(query1)
 
conn.execute(fruits.insert(), [
    {'id' : '76', 'name' : 'kruske', 'price_per_kg':'60'},
     {'id' : '54', 'name' : 'jagode', 'price_per_kg':'100'}

])
 

s = fruits.select()
data = conn.execute(s).fetchall()
print(data)