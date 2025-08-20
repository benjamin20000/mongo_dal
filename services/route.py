from bson import ObjectId
from fastapi import FastAPI, HTTPException
from dal import get_all, get_soldier_by_id
from services.dal import delete_by_id
from soldier import Soldier

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
    all_sol = get_all()
    return {"soldiers": all_sol}

@app.post("/soldier_by_id")
def soldier_by_id(id: str):
    try:
        object_id = ObjectId(id)

    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ObjectId")

    soldier = get_soldier_by_id(object_id)

    if not soldier:
        raise HTTPException(status_code=404, detail="Soldier not found")

    soldier["_id"] = str(soldier["_id"])
    return {"soldier":soldier}

@app.delete("/delete_by_id")
def delete_soldier_by_id(id : str):
    try:
        object_id = ObjectId(id)

    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ObjectId")

    soldier = delete_by_id(object_id)

    if not soldier:
        raise HTTPException(status_code=404, detail="Soldier not found")

    return {"status": "Deleted successfully"}