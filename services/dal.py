import pymongo
from bson import ObjectId

class DAl:
    def __init__(self):
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/") ## make connection
        self.mydb = mydb = self.myclient["enemy_soldiers"]  ## init the db
        self.mycol = self.mycol = mydb["soldier_details"]  ##init the collection

    def insert_dic(self ,dic):
        sol_id  = self.mycol.insert_one(dic) ##insert the  soldier
        return str(sol_id.inserted_id)


    def get_all(self):
        res = []
        for sol in self.mycol.find({},{"_id":0}):
            res.append(sol)
        return res

    def get_soldier_by_id(self ,id : ObjectId):

        soldier = self.mycol.find_one({"_id":id})
        return soldier

    def delete_by_id(self , id : ObjectId):

        result = self.mycol.delete_one({"_id": id})
        return result.deleted_count

    def update_soldier_by_id(self ,id: ObjectId, update_fields: dict):

        result = self.mycol.update_one({"_id": id}, {"$set": update_fields})
        return result.modified_count