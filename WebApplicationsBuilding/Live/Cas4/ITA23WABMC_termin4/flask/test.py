from DBcm import UseDatabase  # , SQLError
 
config = {'host': '127.0.0.1',
          'user': 'root',
          'password': '',
          'database': 'vsearchlogDB',
          'port': 3307}
 
with UseDatabase(config) as cursor:
    _SQL = "select * from log"
    cursor.execute(_SQL)
    data = cursor.fetchall()
    print(data)