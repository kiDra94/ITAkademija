'''
Zadatak 1.7. Izvršiti translakciju od 100.0 sa računa A na račun B, 
                      translakciju od 200.0 sa računa B na račun C
                    I translakciju od 300.0 sa računa C na račun A.
Postaviti da sva tri računa na početku imaju po 300.0.'''


import sqlite3
 
conn = sqlite3.connect('accounts.db')
cursor = conn.cursor()
 
try:
    cursor.execute("""CREATE TABLE IF NOT EXISTS accounts (
                        name TEXT NOT NULL PRIMARY KEY,
                        balance FLOAT NOT NULL)""")
    account = [('A',300.0), ('B', 300.0),('C',300.0)]
   

    cursor.executemany("INSERT INTO accounts VALUES (?, ?)", account)
    conn.commit()
    
    cursor.execute("UPDATE accounts SET balance = balance - 100.0 "
    "WHERE name = 'A'")
    cursor.execute("UPDATE accounts SET balance = balance + 100.0 "
    "WHERE name = 'B'")
    conn.commit()

    cursor.execute("UPDATE accounts SET balance = balance - 200.0 "
    "WHERE name = 'B'")
    cursor.execute("UPDATE accounts SET balance = balance + 200.0 "
    "WHERE name = 'C'")
    conn.commit()

    cursor.execute("UPDATE accounts SET balance = balance - 300.0 "
    "WHERE name = 'C'")
    cursor.execute("UPDATE accounts SET balance = balance + 300.0 "
    "WHERE name = 'A'") 
    conn.commit()

    conn.commit()
    print('Transaction committed!')
 
except conn.Error:
    conn.rollback()
    print('Transaction rolledback!')