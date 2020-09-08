# Questions for Today

"""How many total Characters are there?
How many of each specific subclass?
How many Items are there?
How many of the Items are weapons? How many are not?
How many Items does each character have? (Return first 20 rows)
How many Weapons does each character have? (Return first 20 rows)
On average, how many Items does each Character have?
On average, how many Weapons does each character have?"""

import sqlite3


conn = sqlite3.connect('../module3-nosql-and-document-oriented-databases/rpg_db.sqlite3')
curs = conn.cursor()


"""How many total Characters are there"""
character_query = 'SELECT COUNT(*) FROM charactercreator_character'
curs.execute(character_query)
results = curs.fetchone() # fetchall() is somewhat interchangeable
print(f"Total Characters: {results[0]}")


"""
How Many of Each Specific subclass
"""
cleric_query = 'SELECT COUNT(*) FROM charactercreator_cleric'
curs.execute(cleric_query)
cleric_results = curs.fetchone()
print(f"Number of Cleric Subclass: {cleric_results[0]}")

fighter_query = 'SELECT COUNT(*) FROM charactercreator_fighter'
curs.execute(fighter_query)
fighter_results = curs.fetchone()
print(f"Number of Fighter Subclass: {fighter_results[0]}")

mage_query = 'SELECT COUNT(*) FROM charactercreator_mage'
curs.execute(mage_query)
mage_results = curs.fetchone()
print(f"Number of Mage Subclass: {mage_results[0]}")

necromancer_query = 'SELECT COUNT(*) FROM charactercreator_necromancer'
curs.execute(necromancer_query)
necromancer_results = curs.fetchone()
print(f"Number of Necromancer Subclass: {necromancer_results[0]}")

thief_query = 'SELECT COUNT(*) FROM charactercreator_thief'
curs.execute(thief_query)
thief_results = curs.fetchone()
print(f"Number of Thief Subclass: {thief_results[0]}")


"""
How many Items are there?
"""
armor_query = 'SELECT COUNT(*) FROM armory_item'
curs.execute(armor_query)
items_results = curs.fetchone()
print(f"Number of Items in Armory: {items_results[0]}")

"""
How many of the Items are weapons? How many are not?
"""
weapon_query = 'SELECT COUNT(*) FROM armory_weapon'
curs.execute(weapon_query)
weapon_results = curs.fetchone()
print(f"Number of Weapons in Armory: {weapon_results[0]}")
print(f"Not Weapons: {items_results[0] - weapon_results[0]}")


"""
How many Items does each character have? (Return first 20 rows)
"""
item_per_character = """SELECT character_id, COUNT(DISTINCT item_id) 
#Distinct means Unqiue or Value_counts

#subquery below
FROM(SELECT cc.character_id, cc.name AS character_name, ai.item_id, ai.name AS item_name
FROM charactercreator_character AS cc,armory_item AS ai, charactercreator_character_inventory AS cci
WHERE cc.character_id = cci.character_id AND ai.item_id = cci.item_id) ###This WHERE function is the implicit join
GROUP BY 1 ORDER BY 2 DESC #Group by column 1, and Column 2 becomes descending column with items
LIMIT 20;"""
curs.execute(item_per_character)
item_per_character_results = curs.fetchall()
print(f"Total Items for Each Character: {item_per_character_results}")


"""
How many Weapons does each character have? (Return first 20 rows)
"""
weapon_per_character = """SELECT name, COUNT(DISTINCT item_ptr_id) FROM
(SELECT cc.character_id, cc.name, aw.item_ptr_id, aw.power
FROM charactercreator_character AS cc,
armory_weapon AS aw,
charactercreator_character_inventory AS cci
WHERE cc.character_id = cci.character_id
AND aw.item_ptr_id = cci.item_id)
GROUP BY 1 ORDER BY 2 DESC
LIMIT 20;"""
curs.execute(weapon_per_character)
weapon_per_character_result = curs.fetchall()
print(f"Total Weapons for Characters: {weapon_per_character_result}")

