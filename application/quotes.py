from fastapi import FastAPI, status
from .models import Quote


app = FastAPI()

QUOTES_DB = {
    "forty_two": "The answer to life the universe and everything",
    "harry_met_sally": "I'll have what she's having"
}


@app.get("/")
def home():
    return "Welcome to the Quotes Library!"


@app.get("/quotes")
def list_quotes():
    return QUOTES_DB


@app.get("/quotes/{item_id}")
def quote_detail(item_id: str):
    detail = {
        "quote_id": item_id,
        "quote": QUOTES_DB[item_id]
    }
    return detail


@app.post("/quotes", status_code=status.HTTP_201_CREATED)
def create_quote(item: Quote):
    QUOTES_DB[item.name] = item.message
    return {"message": f"Quote '{item.name}' was created!"}