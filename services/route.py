from bson import ObjectId
from fastapi import FastAPI, HTTPException
from dal import DAl
from soldier import Soldier


dal = DAl()
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/soldier")
def insert_sol(first_name, last_name, phone_number, rank):
    new_soldier = Soldier(first_name, last_name, phone_number, rank)
    id = new_soldier.insert_soldier_to_db()
    return {"id": id}

@app.get("/soldiers")
def read_item():
    all_sol = dal.get_all()
    return {"soldiers": all_sol}

@app.post("/soldier_by_id")
def soldier_by_id(id: str):
    try:
        object_id = ObjectId(id) # type id in mongodb

    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ObjectId")

    soldier = dal.get_soldier_by_id(object_id)

    if not soldier:
        raise HTTPException(status_code=404, detail="Soldier not found")

    soldier["_id"] = str(soldier["_id"])
    return {"soldier":soldier}

@app.delete("/delete_soldier_by_id")
def delete_soldier_by_id(id : str):
    try:
        object_id = ObjectId(id) # type id in mongodb

    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ObjectId")

    soldier = dal.delete_by_id(object_id)

    if soldier == 0:
        raise HTTPException(status_code=404, detail="Soldier not found")

    return {"status": "Deleted successfully"}

@app.put("/update_soldier")
def update_soldier(id: str, first_name: str = None, last_name: str = None, phone_number: int = None, rank: int = None):
    try:
        object_id = ObjectId(id) # type id in mongodb
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ObjectId")

    update_fields = {}
    if first_name is not None:
        update_fields["first_name"] = first_name
    if last_name is not None:
        update_fields["last_name"] = last_name
    if phone_number is not None:
        update_fields["phone_number"] = phone_number
    if rank is not None:
        update_fields["rank"] = rank

    if not update_fields:
        raise HTTPException(status_code=400, detail="No fields to update")

    modified_count = dal.update_soldier_by_id(object_id, update_fields)


    if modified_count == 0:
        raise HTTPException(status_code=404, detail="Soldier not found or no changes applied")

    return {"status": "Updated successfully", "updated_fields": update_fields}