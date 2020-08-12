import sqlite3
import psycopg2

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

get_characters = "SELECT * FROM charactercreator_character;"
sl_curs.execute(get_characters)
characters = sl_curs.fetchall()
# print(characters)

# print(len(characters))

#print(characters[:5])

sl_curs.execute('PRAGMA table_info(charactercreator_character);')
sl_curs.fetchall()
#print(sl_curs.fetchall())

create_character_table = """
CREATE TABLE charactercreator_character (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    level INT,
    exp INT,
    hp INT, 
    strength INT, 
    intelligence INT,
    dexterity INT, 
    wisdom INT
);
"""

dbname = "nsvkevhb"
user = "nsvkevhb"
password = "mTsryvpzvKAG_GuZ6DEGn1K0ZcT4PvbZ"
host = "otto.db.elephantsql.com"

# Defining a function to refresh connection and cursor
def refresh_connection_and_cursor(conn, curs):
    curs.close()
    conn.close()
    pg_conn = psycopg2.connect(dbname=dbname, user=user,
                             password=password, host=host)
    pg_curs = pg_conn.cursor()
    return pg_conn, pg_curs


pg_conn, pg_curs = refresh_connection_and_cursor(sl_conn, sl_curs)

#print(characters[0])

for character in characters:
    insert_character = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES """ + str(character[1:]) + ";"
pg_curs.execute(insert_character)

pg_conn.commit()


# Let's look at what we've done
pg_curs.execute('SELECT * FROM charactercreator_character LIMIT 5;')
print(pg_curs.fetchall())


pg_curs.close()
pg_conn.close()
sl_curs.close()
sl_conn.close()
