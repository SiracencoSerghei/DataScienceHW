from pymongo import MongoClient

import os
from dotenv import load_dotenv

load_dotenv()

db_uri = os.getenv("MONGODB_URI")
db_name = os.getenv("DB_NAME")

# print("DB URI:", db_uri)
# print("DB NAME:", db_name)

# Підключення до MongoDB
client = MongoClient(db_uri)
db = client[db_name]

# Перевірка
# stats = db.command("collstats", "cats")
# print("Статистика колекції 'cats':", stats)

# Додати перший документ до колекції "cats"
cat_doc = {
    "name": "barsik",
    "age": 3,
    "features": ["ходить в капці", "дає себе гладити", "рудий"],
}
db.cats.insert_one(cat_doc)


print("Колекції в базі:", db.list_collection_names())
print("Документи в 'cats':", list(db.cats.find()))
