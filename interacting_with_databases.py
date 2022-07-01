"""
In a business setting, most data may not be stored in text or Excel files.
SQL-based relational databases (such as SQL Server, PostgreSQL, and
MySQL) are in wide use, and many alternative databases have become
quite popular. The choice of database is usually dependent on the
performance, data integrity, and scalability needs of an application.
pandas has some functions to simplify loading the results of a SQL query
into a DataFrame. As an example, I’ll create a SQLite database using
Python’s built-in sqlite3 driver:
"""
import sqlite3
import pandas as pd

query = "CREATE TABLE test (a VARCHAR(20), b VARCHAR(20), c REAL, d INTEGER);"

con = sqlite3.connect('mydata.sqlite')

con.execute(query)

con.commit()

data = [('Atlanta', 'Georgia', 1.25, 6),
        ('Tallahassee', 'Florida', 2.6, 3),
        ('Sacramento', 'California', 1.7, 5)]

stmt = "INSERT INTO test VALUES(?, ?, ?, ?)"

con.executemany(stmt, data)

con.commit()

# Most Python SQL drivers (PyODBC, psycopg2, MySQLdb, turbodbc, etc.)
# return a list of tuples when selecting data from a table:
cursor = con.execute('select * from test')

rows = cursor.fetchall()

print(rows)

print(cursor.description)
p_data = pd.DataFrame(rows, columns=[x[0] for x in cursor.description])
print(p_data)

# pandas has a read_sql function that enables you to read data
# easily from a general SQLAlchemy connection
"""
import sqlalchemy as sqla
db = sqla.create_engine('sqlite:///mydata.sqlite')
pd.read_sql('select * from test', db)
"""
