from fastapi import FastAPI


app = FastAPI()

QUOTES_DB = {
    "forty_two": "The answer to life the universe and everything",
    "harry_met_sally": "I'll have what she's having"
}

@app.get("/")
def hello():
    return {"hello": "world"}