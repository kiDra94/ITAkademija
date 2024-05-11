from DBcm import UseDatabase  # , SQLError

config = {'host': '127.0.0.1',
          'user': 'root',
          'password': 'banjalukA1%',
          'database': 'vsearchlogDB',
          'port': 3306}

with UseDatabase(config) as cursor:
    _SQL = "select * from log"
    cursor.execute(_SQL)
    data = cursor.fetchall()
    print(data)