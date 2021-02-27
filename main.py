from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

QUOTES_DB = {
    "forty_two": "The answer to life the universe and everything",
    "harry_met_sally": "I'll have what she's having"
}


class Quote(BaseModel):
    name: str
    message: str


@app.get("/")
def hello():
    return {"hello": "world"}


@app.get("/quotes")
def list_quotes():
    all_quotes = {quote: QUOTES_DB[quote] for quote in QUOTES_DB}
    return all_quotes


@app.get("/quotes/{item_id}")
def quote_detail(item_id: str):
    detailed = {"quote_id": item_id, "quote": QUOTES_DB[item_id]}
    return detailed