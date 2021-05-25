import json


def read_data():
    db = json.load(open('db.json', 'r'))
    return db


def save_data(data):
    with open('db.json', 'w') as db:
        json.dump(data, db, indent=2)
