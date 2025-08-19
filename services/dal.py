import pymongo


def insert_dic(dic):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")  ## make connection
    mydb = myclient["enemy_soldiers"]  ## init the db
    mycol = mydb["soldier_details"]  ##init the collection
    ##insert the first soldier
    mycol.insert_one(dic)


def get_all():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["enemy_soldiers"]
    mycol = mydb["soldier_details"]
    res = []
    for sol in mycol.find():
        res.append(sol)
    return res

