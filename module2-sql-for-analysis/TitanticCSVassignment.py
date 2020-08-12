import pandas as pd
import psycopg2

df = pd.read_csv('titanic.csv')
df = df.rename({'Siblings/Spouses Aboard': 'SibSpouse',
                'Parents/Children Aboard': 'ParChild'}, axis=1)

#print(df.head())

cloud = psycopg2.connect(
    dbname="nsvkevhb",
    user="nsvkevhb",
    password="mTsryvpzvKAG_GuZ6DEGn1K0ZcT4PvbZ",
    host="otto.db.elephantsql.com",
)

cursor = cloud.cursor()

cursor.execute("""
DROP TABLE IF EXISTS Titanic;
CREATE TABLE Titanic (
    Survived        INT8,
    Pclass          INT8,
    SibSpouse       INT8,
    ParChild        INT8,
    FARE            FLOAT8);
""")
cloud.commit()

cursor.execute("""
SELECT
FROM Titanic
LIMIT 1;
""")

print(cursor.fetchone())

# Dont understand why I am not receiving any values from the above statement
# Seems like it executed fine, but im starting to think my DF has no values at all
