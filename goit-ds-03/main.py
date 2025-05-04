import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

# Підключення до MongoDB
db_uri = os.getenv("MONGODB_URI")  
db_name = os.getenv("DB_NAME")  
client = MongoClient(db_uri, server_api=ServerApi('1'))
db = client[db_name]
cats_collection = db.cats 
# print(dir(cats_collection))
# help(cats_collection)
# for cat in cats_collection.find():
#     print(cat)

def read_all_cats():
    """
    Функція для читання всіх котів з колекції cats.
    """
    cats = []
    for cat in cats_collection.find():
        cats.append(cat)
    return cats
# print(read_all_cats())

def read_cat_by_name(name):
    """
    Функція для читання кота за його ім'ям.
    """
    cat = cats_collection.find_one({"name": name})
    if cat:
        return cat
    else:
        return None
# print(read_cat_by_name("Tommy"))

def update_cat_age_by_name(name, new_age):
    """
    Функція для оновлення віку кота за його ім'ям.
    """
    result = cats_collection.update_one(
        {"name": name},
        {"$set": {"age": new_age}}
    )
    return cats_collection.find_one({"name": name})

def add_cat_feature(name, feature):
    """
    Функція для додавання нової особливості коту за його ім'ям.
    """
    result = cats_collection.update_one(
        {"name": name},
        {"$addToSet": {"features": feature}}
    )
    return cats_collection.find_one({"name": name})
# print(add_cat_feature("Tommy", "playful"))


def delete_cat_by_name(name):
    """
    Функція для видалення кота за його ім'ям та повернення видаленого імені.
    """
    cat = cats_collection.find_one({"name": name})
    if cat:
        cats_collection.delete_one({"name": name})
        return cat["name"]
    else:
        return "Кота з таким іменем не знайдено"  # або None


# print(delete_cat_by_name("Tommy"))

def delete_all_cats():
    """
    Функція для видалення всіх котів з колекції cats.
    """
    result = cats_collection.delete_many({})
    return result.deleted_count
# print(delete_all_cats())


def add_new_cat(name, age, features):
    """
    Функція для додавання нового кота до колекції cats.
    Повертає дані доданого кота.
    """
    new_cat = {"name": name, "age": age, "features": features}
    cats_collection.insert_one(new_cat)
    return new_cat


# print(add_new_cat("Tommy", 3, ["playful", "friendly"]))
def main():
    # Приклад використання функцій
    print("All cats:", read_all_cats())
    print("Cat by name:", read_cat_by_name("Tommy"))
    print("Update cat age:", update_cat_age_by_name("Tommy", 5))
    print("Add cat feature:", add_cat_feature("Tommy", "smart"))
    print("Delete cat by name:", delete_cat_by_name("Tommy"))
    print("Delete all cats:", delete_all_cats())
    print("Add new cat:", add_new_cat("Tommy", 3, ["playful", "friendly", "smart", "cute", "lazy"]))
if __name__ == "__main__":
    main()
