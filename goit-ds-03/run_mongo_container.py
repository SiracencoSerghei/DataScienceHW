import docker
import time
import os


def run_mongo_container():
    client = docker.from_env()  # Підключення до Docker

    # Перевірка наявності контейнера
    try:

        container = client.containers.get("mongo")
        if container.status != "running":
            print("Контейнер існує, але не працює. Перезапускаємо...")
            container.start()
        print("Контейнер MongoDB вже працює.")
    except docker.errors.NotFound:
        # Запуск контейнера MongoDB
        print("Запуск контейнера MongoDB...")

        # Створення локальної папки для даних, якщо вона не існує
        local_data_path = os.path.abspath("./mongo_data")  # Отримуємо абсолютний шлях
        os.makedirs(
            local_data_path, exist_ok=True
        )  # Створює папку, якщо вона ще не існує

        container = client.containers.run(
            "mongo:latest",  # Образ Docker
            name="mongo",  # Ім'я контейнера
            ports={"27017": "27017"},  # Проброс порту
            volumes={
                local_data_path: {"bind": "/data/db", "mode": "rw"}
            },  # Використовуємо volume
            detach=True,  # Запуск в фоновому режимі
        )
        print(f"Контейнер {container.name} успішно запущено.")

    # Чекаємо, поки MongoDB буде готовий до підключення
    print("Очікуємо, поки MongoDB завантажиться...")
    time.sleep(5)  # Додаємо паузу для завантаження MongoDB

    return container


def stop_mongo_container():
    client = docker.from_env()
    try:
        container = client.containers.get("mongo")
        if container.status == "running":
            print("Зупиняємо контейнер MongoDB...")
            container.stop()
            print("Контейнер зупинено.")
        else:
            print("Контейнер вже зупинений.")
    except docker.errors.NotFound:
        print("Контейнер 'mongo' не знайдено.")


if __name__ == "__main__":
    container = run_mongo_container()
    # stop_mongo_container()
