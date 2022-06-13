from tinydb import TinyDB, Query

__db = TinyDB("persist.json")


def get_db():
    return __db.table("polls")
