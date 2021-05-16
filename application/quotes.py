from fastapi import FastAPI, status

from .db import read_data, save_data
from .models import Quote


app = FastAPI()


QUOTES_DB = read_data()


@app.get("/")
def home():
    return "Welcome to the Quotes Library!"


@app.get("/quotes")
async def list_quotes():
    return QUOTES_DB


@app.get("/quotes/{item_id}")
async def quote_detail(item_id: str):
    detail = {
        "quote_id": item_id,
        "quote": QUOTES_DB[item_id]
    }
    return detail


@app.post("/quotes", status_code=status.HTTP_201_CREATED)
async def create_quote(item: Quote):
    QUOTES_DB[item.id] = item.text
    save_data(QUOTES_DB)
    return {"message": f"Quote '{item.id}' was created!"}