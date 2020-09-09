import pymongo

# I think mongo is a bit more complex than sqlite and postgres
# But the benefit is you can do more with mongo and share easier


client = pymongo.MongoClient("mongodb+srv://lpetrus16:WfCtc5j15fDWwmyw@cluster0.oxoh9.gcp.mongodb.net/"
                             + "test?retryWrites=true&w=majority")
db = client.test

rpg_character = (1, "King Bob", 10, 3, 0, 0, 0)

db.test.insert_one(rpg_character)

rpg_doc = {
    'sql_key': rpg_character[0],
    'name': rpg_character[1],
    'hp': rpg_character[2],
    'level': rpg_character[3],
    'health': rpg_character[4],
    'skill': rpg_character[5],
    'dexterity': rpg_character[6]
}
db.test.insert_one(rpg_doc)

print(rpg_doc[0])


