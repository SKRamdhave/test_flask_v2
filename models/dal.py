"""
DAL - Data Access Layer

This module contains code to retrieve and store data (Data Manipulation)

json.load() => to convert json data from "flashcard_db.json" file to List (Python Object)
"""

import json

def load_db():
    file_path = "C:/Users/ADMIN/PycharmProjects/test_flask_v2/models/flashcard_db.json"
    with open(file_path, "r") as foo:
        return json.load(foo)             # to read json data from given file (flashcard_db.json)


db = load_db()               # db = database (List format)


# if __name__ == "__main__":
#    data = load_db()                       # type(data) = List
#    breakpoint()
