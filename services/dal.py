import pymongo
from bson import ObjectId


def insert_dic(dic):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")  ## make connection
    mydb = myclient["enemy_soldiers"]  ## init the db
    mycol = mydb["soldier_details"]  ##init the collection
    sol_id  =mycol.insert_one(dic) ##insert the  soldier
    return str(sol_id.inserted_id)


def get_all():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["enemy_soldiers"]
    mycol = mydb["soldier_details"]
    res = []
    for sol in mycol.find({},{"_id":0}):
        res.append(sol)
    return res

def get_soldier_by_id(id : ObjectId):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["enemy_soldiers"]
    mycol = mydb["soldier_details"]

    soldier = mycol.find_one({"_id":id})
    return soldier

def delete_by_id(id : ObjectId):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["enemy_soldiers"]
    mycol = mydb["soldier_details"]

    result = mycol.delete_one({"_id": id})
    if result.deleted_count == 0:
        return False
    return True