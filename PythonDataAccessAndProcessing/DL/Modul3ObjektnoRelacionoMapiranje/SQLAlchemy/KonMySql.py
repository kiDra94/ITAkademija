from sqlalchemy import create_engine
engine = create_engine("mysql://user:pwd@localhost/example",echo = True)