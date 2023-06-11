import uvicorn

from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel


client = MongoClient('mongodb://db:27017/')
db = client['mydatabase']
collection = db['mycollection']
app = FastAPI()

class Item(BaseModel):
    name: str
    description: str
    price: float


def get_obj_from_obj_mongo(mongo_obj):
    id_mongo_obj = str(mongo_obj['_id'])
    del mongo_obj['_id']
    mongo_obj['id_'] = id_mongo_obj
    return mongo_obj


@app.get('/items/')
async def read_items():
    items = collection.find()
    return [get_obj_from_obj_mongo(item) for item in items]


@app.post('/items/')
async def create_item(item: Item):
    result = collection.insert_one(item.dict())
    return str(result.inserted_id)

