from sqlalchemy.orm import sessionmaker
import sqlalchemy as db
from sqlalchemy import text, String, ForeignKey, Table, Column, Integer, ForeignKeyConstraint, select, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declarative_base, relationship, Session

engine = db.create_engine('mysql+pymysql://root:@localhost:3306/off2')

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30))
    age: Mapped[int] = mapped_column(Integer)

    fees = relationship("Fee")


class Fee(Base):
    __tablename__ = 'fees'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    amount: Mapped[int] = mapped_column(Integer)
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"))


Base.metadata.create_all(engine)

# now let us insert some data into these tables and then query the data with the relationship

with Session(engine) as session:

    s1 = Student(name='John Doe', age=20)
    print(s1.id)
    session.add(s1)
    session.commit()  # tek kada ovo uradimo uspostavlja se relacija izmedju podatka u bazi (students.id) i atributa s1.id
    print(s1.id)
    f1 = Fee(amount=100, student_id=s1.id)
    f2 = Fee(amount=200, student_id=s1.id)
    session.add_all([f1, f2])

    print("Medju ispis pre commit-a")
    s1.fees.append(f1)
    s1.fees.append(f2)
    for i in s1.fees:
        print(i.amount)

    session.commit()

    student_fees = session.query(Student).all()

    # ispis studentskih tarifa
    for student in student_fees:
        for fee in student.fees:
            print(fee.amount)
