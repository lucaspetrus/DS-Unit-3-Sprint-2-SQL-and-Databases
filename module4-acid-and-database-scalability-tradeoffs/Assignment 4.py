import psycopg2
import pandas as pd


df = pd.read_csv('titanic.csv')
df = df.rename({'Siblings/Spouses Aboard': 'SibSpouse',
                'Parents/Children Aboard': 'ParChild'}, axis=1)


cloud = psycopg2.connect(
    dbname="nsvkevhb",
    user="nsvkevhb",
    password="mTsryvpzvKAG_GuZ6DEGn1K0ZcT4PvbZ",
    host="otto.db.elephantsql.com",
)


curs = cloud.cursor()

# Survived,Pclass,Name,Sex,Age,Siblings/Spouses Aboard,Parents/Children Aboard,Fare


curs.execute("""
DROP TABLE IF EXISTS Titanic;
CREATE TABLE Titanic (
    Survived        bool,
    Pclass          INT8,
    Name            text,
    Sex             text,
    Age             FLOAT8,
    SibSpouse       INT8,
    ParChild        INT8,
    FARE            FLOAT8);
""")
cloud.commit()

with open('titanic.csv', 'r') as f:
    next(f)
    curs.copy_from(f, 'Titanic', sep=',')

cloud.commit()

survivor_query = """SELECT COUNT (*) 
                    FROM Titanic
                    WHERE Survived = '1'  """
curs.execute(survivor_query)
items_results = curs.fetchone()
print(f"Number of Survivors: {items_results[0]}")

cloud.commit()


class_query = """SELECT Pclass, COUNT(*)
                FROM Titanic
                GROUP BY Pclass"""
curs.execute(class_query)
items_results = curs.fetchall()
print(f"Different Classes: {items_results}")

cloud.commit()


# How many passengers survived/died within each class?

survived_class_query = """SELECT COUNT(*)
                FROM Titanic
                WHERE Survived = True
                GROUP BY Pclass
                """
curs.execute(survived_class_query)
items_results = curs.fetchall()
print(f"Survived Classes: {items_results}")

died_class_query = """SELECT COUNT(*)
                FROM Titanic
                WHERE Survived = False
                GROUP BY Pclass
                """
curs.execute(died_class_query)
items_results = curs.fetchall()
print(f"Dead Classes: {items_results}")


# What was the average age of survivors vs nonsurvivors?
average_age_survivor_query = """SELECT AVG(age), Survived
FROM Titanic
WHERE Survived = True
GROUP BY Survived
"""
curs.execute(average_age_survivor_query)
items_results = curs.fetchone()
print(f"Average Age of Survivors: {items_results[0]}")