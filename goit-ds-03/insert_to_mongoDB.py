import json
import time
from pymongo import MongoClient, UpdateOne
from run_mongo_container import run_mongo_container

# Step 1: Start or get the Mongo container
container = run_mongo_container()

# Step 2: Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.scraped_data  # Database name = scraped_data

# Step 3: Ensure collections exist
if "quotes" not in db.list_collection_names():
    db.create_collection("quotes")
if "authors" not in db.list_collection_names():
    db.create_collection("authors")

quotes_col = db.quotes
authors_col = db.authors

# Step 4: Load JSON data
with open("quotes.json", "r", encoding="utf-8") as f:
    quotes = json.load(f)

with open("authors.json", "r", encoding="utf-8") as f:
    authors = json.load(f)

# Step 5: Insert or update authors
author_ops = [
    UpdateOne({"name": author["name"]}, {"$set": author}, upsert=True)
    for author in authors
]

if author_ops:
    result = authors_col.bulk_write(author_ops)
    print(
        f"Authors upserted: {result.upserted_count}, modified: {result.modified_count}"
    )

# Step 6: Insert or update quotes
quote_ops = [
    UpdateOne(
        {"quote": quote["quote"], "author": quote["author"]},
        {"$set": quote},
        upsert=True,
    )
    for quote in quotes
]

if quote_ops:
    result = quotes_col.bulk_write(quote_ops)
    print(
        f"Quotes upserted: {result.upserted_count}, modified: {result.modified_count}"
    )
# Step 7: Close the connection
client.close()