'''Zadatak 3.1. Korišćenjem SQLAlchemy okvira i SQLite baze podataka kreirati tabelu People koja će sadržati sledeće kolone:
    • personal_number – primarni ključ;
    • first_name – text;
    • last_name – text;
    • year_of_birth – int;
    • city – text;
Neophodno je prikazati unošenje više osoba i čitanje svih osoba iz tabele People.'''

#importovanje metode create_engine, objekata Metadata,Table i Column kao i genericke tipove 
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

#kreiranje engine objekta, prosledjuje se baza, drugi argument-echo ako je True  to znači da će se na ekranu ispisivati rezultati svih izvršenih upita.
engine = create_engine('sqlite:///assigment.db', echo = False)

#Kreiranje instance MetaData objekta koji sluzi za povezivanje sa semom
meta = MetaData()

#pravljenje tabele
assigmentTB = Table(
   'People', meta, 
   Column('personal_number', Integer, primary_key = True), 
   Column('first_name', String),
   Column('last_name', String), 
   Column('year_of_birth', Integer),
   Column('city', String)
)

#ovom metodom cemo narediti kreiranje definisane tabele.
meta.create_all(engine)
 
#unos podataka
People_personal_number = int(input("Ukucajte personalni broj: "))
People_first_name = input("Ukucajte ime: ")
People_last_name = input("Ukucajte prezime: ")
People_year_of_birth = int(input("Ukucajte godinu rodjenja: "))
People_city = input("Ukucajte grad: ")

#kreira se insert upit koji ubacuje podatke
query = assigmentTB.insert().values(personal_number = People_personal_number, first_name= People_first_name, last_name = People_last_name, year_of_birth=People_year_of_birth, city=People_city)

# kreira se upit koji ce iscitati sve podatke iz baze
query2 = assigmentTB.select()

#Da bi se prikazani upiti izvršili, neophodno je da imamo aktivno provereni izvor DB-API veze,
conn = engine.connect()

#izvrsavanje upita
r1 = conn.execute(query)
result = conn.execute(query2)

#ispis podataka
for row in result:
    print("Personal number: {} | First name: {} | Last name: {} | Year of birth: {} | City: {}".format(row[0], row[1], row[2], row[3], row[4]))