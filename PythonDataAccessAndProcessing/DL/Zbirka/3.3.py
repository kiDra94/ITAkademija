from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
 
engine = create_engine('sqlite:///example.db', echo = True)
meta = MetaData()
 
cars = Table(
   'Cars', meta, 
   Column('license plate', String, primary_key = True), 
   Column('brand', String), 
   Column('model', String),
   Column('year',Integer)
)
 
meta.create_all(engine)
 
Car_license_plate =input("Ukucajte registarsku tablicu: ")
Car_brand = input("Ukucajte marku: ")
Car_model = input("Ukucajte model: ")
Car_year=int(input("Ukucajte godinu: "))

query = cars.insert().values(license_plate = Car_license_plate, brand= Car_brand, model = Car_model, year=Car_year)

query2 = cars.select()
 
conn = engine.connect()

r1 = conn.execute(query)
result = conn.execute(query2)
 
for row in result:
    print("Licence plate: {} | Brand: {} | Model: {} | Year: {}".format(row[0], row[1], row[2], row[3]))
 