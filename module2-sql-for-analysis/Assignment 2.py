import psycopg2

dbname = "nsvkevhb"
user = "nsvkevhb"
password = "mTsryvpzvKAG_GuZ6DEGn1K0ZcT4PvbZ"
host = "otto.db.elephantsql.com"

connection = psycopg2.connect(dbname=dbname, user=user,
                              password=password, host=host)

cursor = connection.cursor('titantic.csv')

