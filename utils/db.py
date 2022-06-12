from tinydb import TinyDB

__db = TinyDB("persist.json")

def get_db():
    return __db.table("polls")