from tinydb import TinyDB, Query

__db = TinyDB("persistence.json")


def get_db():
    return __db.table("polls")
