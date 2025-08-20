from dal import insert_dic


class Soldier:
    def __init__(self , first_name , last_name , phone_number , rank, id = None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.rank = rank

    def insert_soldier_to_db(self):
        soldier = {"first_name": self.first_name, "last_name": self.last_name, "phone_number": self.phone_number, "rank": self.rank}
        insert_dic(soldier)





