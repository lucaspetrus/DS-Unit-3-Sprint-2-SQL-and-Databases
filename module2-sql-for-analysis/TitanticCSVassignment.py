import sqlite3

import psycopg2

# help(psycopg2.connect)
dbname = "nsvkevhb"
user = "nsvkevhb"
password = "mTsryvpzvKAG_GuZ6DEGn1K0ZcT4PvbZ"
host = "otto.db.elephantsql.com"


conn = sqlite3.connect('/Users/lucaspetrus/PycharmProjects/DS-Unit-3-Sprint-2-SQL-and-Databases/module2-sql-for-analysis/titanic.csv')
curs = conn.cursor()

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)
dir(conn)

