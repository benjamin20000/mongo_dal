import pymongo


def init_db_and_collection():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["enemy_soldiers"] ## init the db
    mycol = mydb["soldier_details"]  ##init the collection
    ##create the first soldier
    first_soldier = { "first_name": "John","last_name":"John","phone_number":123, "rank":1 }
    ##insert the first soldier
    mycol.insert_one(first_soldier)