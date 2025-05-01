import sqlite3
from sql_requests import requests

# Підключення до бази даних
conn = sqlite3.connect("todo.db")
cursor = conn.cursor()


def main():
    while True:
        print("\nОберіть запит (або 0 для виходу):")
        for i, req in enumerate(requests):
            print(f"{i + 1}. {req[0]}")
        choice = input("Ваш вибір: ")
        if not choice.isdigit() or int(choice) == 0:
            break
        index = int(choice) - 1
        if 0 <= index < len(requests):
            selected = requests[index]
            sql = selected[1]
            prompts = selected[2:] if len(selected) > 2 else []

            params = []
            for prompt in prompts:
                user_input = input(f"{prompt}: ")
                params.append(user_input)

            if "fullname = ?" in sql and "NOT EXISTS" in sql and len(params) == 2:
                params += [params[0], params[1]]
                
            try:
                cursor.execute(sql, tuple(params))
                if sql.strip().lower().startswith("select"):
                    results = cursor.fetchall()
                    for row in results:
                        print(row)
                else:
                    conn.commit()
                    print("Запит виконано успішно.")
            except Exception as e:
                print("Помилка:", e)
        else:
            print("Невірний вибір!")

if __name__ == "__main__":
    main()
