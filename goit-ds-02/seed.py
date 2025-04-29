from datetime import datetime
from random import randint, choice
import sqlite3
from faker import Faker

NUMBER_OF_USERS = 100
NUMBER_OF_TASKS = 200
STATUSES = [("new",), ("in progress",), ("completed",)]


def create_unique_email(emails):
    fake = Faker()
    while True:
        email = fake.email()
        if email not in emails:
            emails.add(email)
            return email


def generate_fake_data(number_of_users, number_of_tasks):
    fake = Faker()
    emails = set()
    users = []
    tasks = []

    # Генерація користувачів
    for _ in range(number_of_users):
        name = fake.name()
        email = create_unique_email(emails)
        users.append((name, email))

    # Генерація завдань
    for _ in range(number_of_tasks):
        title = fake.sentence(nb_words=4).rstrip(".")
        description = fake.paragraph(nb_sentences=2)
        tasks.append((title, description))

    return users, tasks


def insert_data_to_db(users, tasks):
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()

    # Вставка користувачів
    cursor.executemany("INSERT INTO users (fullname, email) VALUES (?, ?)", users)

    # Вставка статусів (якщо їх ще немає)
    cursor.executemany("INSERT OR IGNORE INTO status (name) VALUES (?)", STATUSES)

    # Отримання кількості користувачів і статусів
    user_count = len(users)
    status_count = len(STATUSES)

    # Вставка завдань
    for title, description in tasks:
        user_id = randint(1, user_count)
        status_id = randint(1, status_count)
        cursor.execute(
            "INSERT INTO tasks (title, description, status_id, user_id) VALUES (?, ?, ?, ?)",
            (title, description, status_id, user_id),
        )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    users, tasks = generate_fake_data(NUMBER_OF_USERS, NUMBER_OF_TASKS)
    insert_data_to_db(users, tasks)
    print("Seed completed successfully.")
