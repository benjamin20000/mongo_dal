from fastapi import FastAPI
from soldier import Soldier
from dal import get_all


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/soldier")
def insert_sol(first_name, last_name, phone_number, rank):
    new_soldier = Soldier(first_name, last_name, phone_number, rank)
    id = new_soldier.insert_soldier()
    return {"id": id}

@app.get("/soldiers")
def read_item():
    all_sol = get_all()
    return {"soldiers": all_sol}
