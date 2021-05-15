import databases
from typing import List
from fastapi import FastAPI, status

from .models import Quote
from .migration import DATABASE, QUOTES


app = FastAPI()

database = DATABASE
quotes = QUOTES


@app.on_event("startup")
async def startup():
    await database.connect()
    data = [
        {'id': 0, 'text': "The answer to life the universe and everything"},
        {'id': 1, 'text': "I'll have what she's having"},
    ]
    query = quotes.insert().values(id='?', text='?')
    await database.execute_many(query=query, values=data)


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
    await database.execute(quotes.delete())


@app.get("/")
def home():
    return "Welcome to the Quotes Library!"


@app.get("/quotes", response_model=List[Quote])
async def list_quotes():
    query = quotes.select()
    return await database.fetch_all(query)


@app.get("/quotes/{item_id}")
async def quote_detail(item_id: str):
    query = quotes.select(whereclause=f'id = "{item_id}"')
    last_record_id = await database.fetch_all(query)
    return {"id": last_record_id}


@app.post("/quotes", status_code=status.HTTP_201_CREATED)
async def create_quote(item: Quote):
    query = quotes.insert().values(id=item.id, text=item.text)
    created_quote_id = await database.execute(query=query)
    return {"message": f"Quote '{created_quote_id}' was created!"}