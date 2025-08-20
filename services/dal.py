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
        res = []  # 'res' is a list that will store all the soldiers retrieved from the database
        for sol in self.mycol.find({}, {"_id": 0}):  # Iterate over all documents in the collection, excluding the '_id' field
            res.append(sol)
        return res  # Return the list of all soldiers


    def get_soldier_by_id(self ,id : ObjectId):

        soldier = self.mycol.find_one({"_id":id})
        return soldier # is id return dict else return none

    def delete_by_id(self , id : ObjectId):

        result = self.mycol.delete_one({"_id": id})
        return result.deleted_count # Returns the number of documents that were delete

    def update_soldier_by_id(self ,id: ObjectId, update_fields: dict):

        result = self.mycol.update_one({"_id": id}, {"$set": update_fields})
        return result.modified_count  # Returns the number of documents that were modified