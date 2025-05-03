import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from faker import Faker
import random

# Завантажуємо змінні середовища
load_dotenv()

# Підключення до MongoDB
db_uri = os.getenv("MONGODB_URI")  # Вказуємо URI до вашої MongoDB
db_name = os.getenv("DB_NAME")  # Вказуємо ім'я бази даних
client = MongoClient(db_uri, server_api=ServerApi("1"))
db = client[db_name]
cats_collection = db.cats  # Колекція "cats" в базі даних

# ініціалізація Faker
fake = Faker()


# Генерація фейкових даних для кота
def generate_fake_cat():
    name = fake.first_name()  # Генеруємо ім'я
    age = random.randint(1, 10)  # Генеруємо вік кота від 1 до 10
    features = [
        fake.word()
        for _ in range(random.randint(3, 5))  # Генеруємо 3-5 характеристик кота
    ]
    return {"name": name, "age": age, "features": features}

# Генерація та вставка 10 фейкових котів у колекцію
def insert_fake_cats(num_cats=10):
    for _ in range(num_cats):
        cat = generate_fake_cat()
        cats_collection.insert_one(cat)
        print(f"Вставлено кота: {cat['name']}, вік: {cat['age']}, характеристики: {cat['features']}")
    print(f"Вставлено {num_cats} фейкових котів у колекцію 'cats'.")

if __name__ == "__main__":
    # Перевірка наявності колекції "cats"
    if "cats" in db.list_collection_names():
        print("Колекція 'cats' вже існує.")
    else:
        print("Створюємо колекцію 'cats'.")
        db.create_collection("cats")

    # Вставка фейкових котів
    insert_fake_cats(10)
    # Перевірка
    print("Колекції в базі:", db.list_collection_names())
    print("Документи в 'cats':", list(db.cats.find()))
    # Закриття з'єднання
    client.close()
