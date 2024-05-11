import sqlite3

conn = sqlite3.connect('accounts.db')
cursor = conn.cursor()
 
try:
    cursor.execute("CREATE TABLE IF NOT EXISTS accounts ("
                   "name TEXT NOT NULL PRIMARY KEY,balance FLOAT NOT NULL)")
    account = [('A',100.0), ('B', 100.0)]
    cursor.executemany("INSERT INTO accounts VALUES (?, ?)", account)
    cursor.execute("UPDATE accounts SET balance = balance - 100.0 "
     "WHERE name = 'A'")
    cursor.execute("UPDATE accounts SET balance = balance + 100.0 "
     "WHERE name = 'B'")
    conn.commit()
    print('Transaction committed!')

except conn.Error:
    conn.rollback()
    print('Transaction rolledback!')