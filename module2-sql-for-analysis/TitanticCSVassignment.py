import pandas as pd
import psycopg2

df = pd.read_csv('titanic.csv')
df = df.rename({'Siblings/Spouses Aboard': 'SibSpouse',
                'Parents/Children Aboard': 'ParChild'}, axis=1)


cloud = psycopg2.connect(
    dbname="nsvkevhb",
    user="nsvkevhb",
    password="mTsryvpzvKAG_GuZ6DEGn1K0ZcT4PvbZ",
    host="otto.db.elephantsql.com",
)


cursor = cloud.cursor()

# Survived,Pclass,Name,Sex,Age,Siblings/Spouses Aboard,Parents/Children Aboard,Fare


cursor.execute("""
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
    cursor.copy_from(f, 'Titanic', sep=',')

cloud.commit()


