import pymongo

client = pymongo.MongoClient("mongodb+srv://lpetrus16:WfCtc5j15fDWwmyw@cluster0.oxoh9.gcp.mongodb.net/"
                             + "test?retryWrites=true&w=majority")
db = client.test

rpg_character = (1, "King Bob", 10, 3, 0, 0, 0)

db.test.insert_one(rpg_character)

rpg_doc = {
    'sql_key': rpg_character[0],
    'name': rpg_character[1],
    'hp': rpg_character[2],
    'level': rpg_character[3]
}
db.test.insert_one(rpg_doc)

print(rpg_doc[0])


