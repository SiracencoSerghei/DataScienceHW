# Docker та контейнеризація

![Docker Logo](https://www.docker.com/wp-content/uploads/2022/03/vertical-logo-monochromatic.png)

## Зміст
1. [Основні концепції](#основні-концепції)
2. [Архітектура Docker](#архітектура-docker)
3. [Основні команди](#основні-команди-docker)
4. [Приклади використання](#приклади-використання)
5. [Dockerfile](#dockerfile)
6. [Docker Compose](#docker-compose)
7. [Корисні поради](#корисні-поради)
8. [Типові сценарії](#типові-сценарії)

## Основні концепції

| Термін          | Опис |
|-----------------|------|
| **Docker**      | Платформа для створення, розповсюдження та запуску додатків у контейнерах |
| **Контейнер**   | Ізольоване середовище для запуску додатку з усіма його залежностями |
| **Образ (Image)** | Шаблон для створення контейнерів (read-only) |
| **Dockerfile**  | Інструкції для створення образу |
| **Docker Compose** | Іструмент для оркестрації багатоконтейнерних додатків |

## Архітектура Docker
Клієнт (CLI) ↔ REST API ↔ Демон (Docker Engine)
↕
Реєстри (Docker Hub)


## Основні команди Docker

### Робота з контейнерами
```bash
docker run [опції] образ           # Запустити контейнер
docker start контейнер             # Запустити зупинений контейнер
docker stop контейнер              # Зупинити контейнер
docker restart контейнер           # Перезапустити контейнер
docker rm контейнер                # Видалити контейнер
docker ps                         # Показати запущені контейнери
docker ps -a                      # Показати всі контейнери
docker exec -it контейнер команда  # Виконати команду в контейнері
docker logs контейнер             # Переглянути логи контейнера
```
### Робота з образами

```bash
docker pull образ:тег             # Завантажити образ з реєстру
docker images                     # Показати локальні образи
docker rmi образ                  # Видалити образ
docker build -t ім'я .            # Зібрати образ з Dockerfile
docker push репозиторій/образ:тег # Завантажити образ у реєстр
```

### Мережа та томи
```bash
docker network ls                 # Список мереж
docker volume ls                 # Список томів
```
## Приклади використання
### Запуск контейнера
```bash
docker run -d -p 8080:80 --name my-nginx nginx
-d - запустити у фоновому режимі

-p 8080:80 - зв'язати порт 8080 хоста з портом 80 контейнера

--name - задати ім'я контейнеру
```
### Робота з контейнером
```bash
docker exec -it my-nginx bash     # Увійти в контейнер
docker cp файл контейнер:/шлях    # Копіювати файл в контейнер
docker cp контейнер:/шлях файл    # Копіювати файл з контейнера
```
## Dockerfile
### Приклад базового Dockerfile:

```dockerfile

FROM python:3.10          # Базовий образ
WORKDIR /app              # Робоча директорія
COPY . .                  # Копіювати файли
RUN pip install -r requirements.txt  # Встановити залежності
EXPOSE 5000               # Відкрити порт
CMD ["python", "app.py"]  # Команда для запуску
```
Інструкції Dockerfile:

- FROM - базовий образ

- WORKDIR - робоча директорія

- COPY/ADD - копіювання файлів

- RUN - виконання команд при збірці

- EXPOSE - оголошення портів

- CMD/ENTRYPOINT - команда запуску

- ENV - змінні середовища

- VOLUME - оголошення томів

## Docker Compose
Приклад docker-compose.yml:

```yaml
version: '3'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - .:/app
    depends_on:
      - redis
  redis:
    image: redis
```
Основні команди Compose:

```bash
docker-compose up -d      # Запустити сервіси
docker-compose down       # Зупинити та видалити сервіси
docker-compose ps         # Показати стан сервісів
docker-compose logs       # Показати логи
```
### Корисні поради
1. Використовуйте .dockerignore для виключення непотрібних файлів

2. Для production використовуйте конкретні версії образів (не latest)

3. Мінімізуйте кількість шарів в образах (об'єднуйте RUN команди)

4. Використовуйте багатоетапні збірки для зменшення розміру образів

5. Для даних, що змінюються, використовуйте томи (volumes)

## Типові сценарії
### Розробка веб-додатку
```bash
docker-compose up -d       # Запустити середовище
docker-compose exec web bash  # Увійти в контейнер
docker-compose down        # Зупинити середовище
```
### Розгортання в production
```bash
docker build -t my-app .
docker run -d -p 80:5000 --name app my-app
```
📌 **Підказка:**  Використовуйте --help після будь-якої docker команди для отримання додаткової інформації:

```bash
docker run --help
docker-compose --help
```
markdown
# Docker та контейнеризація - Повний гайд

![Docker Logo](https://www.docker.com/wp-content/uploads/2022/03/vertical-logo-monochromatic.png)

## Зміст
1. [Основні концепції](#основні-концепції)
2. [Встановлення Docker](#встановлення-docker)
3. [Основні команди](#основні-команди)
4. [Робота з образами](#робота-з-образами)
5. [Dockerfile](#dockerfile)
6. [Docker Compose](#docker-compose)
7. [Корисні практики](#корисні-практики)
8. [Приклади використання](#приклади-використання)

## Основні концепції

### Що таке Docker?
Docker - це платформа для контейнеризації додатків, яка дозволяє:
- Пакувати додатки та їх залежності в контейнери
- Забезпечувати однакове середовище виконання на різних системах
- Швидко розгортати та масштабувати додатки

### Ключові компоненти
| Компонент       | Опис                                                                 |
|----------------|----------------------------------------------------------------------|
| **Docker Engine** | Основний рушій для створення та запуску контейнерів                 |
| **Docker Hub**   | Хмарний реєстр для зберігання та обміну образами                    |
| **Docker CLI**   | Інтерфейс командного рядка для взаємодії з Docker                   |

## Встановлення Docker

### Для Windows/macOS
1. Завантажте Docker Desktop з [офіційного сайту](https://www.docker.com/products/docker-desktop)
2. Встановіть з стандартними налаштуваннями
3. Запустіть та перевірте версію:
```bash
docker --version
```
### Для Linux (Ubuntu)
```bash
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
sudo systemctl enable docker
sudo systemctl start docker
```
## Основні команди
Керування контейнерами
```bash
# Запустити контейнер
docker run -d -p 80:80 --name my_container nginx

# Перелік контейнерів
docker ps -a

# Зупинити/запустити контейнер
docker stop my_container
docker start my_container

# Видалити контейнер
docker rm my_container
```
### Взаємодія з контейнерами
```bash
# Виконати команду в контейнері
docker exec -it my_container bash

# Переглянути логи
docker logs my_container

# Копіювати файли
docker cp file.txt my_container:/path/
```
### Робота з образами
```bash
# Завантажити образ
docker pull ubuntu:20.04

# Список образів
docker images

# Видалити образ
docker rmi ubuntu:20.04

# Зібрати образ з Dockerfile
docker build -t my_image .
```
## Dockerfile
Приклад повноцінного **Dockerfile** для Python додатку:

```dockerfile
# Базовий образ
FROM python:3.9-slim

# Метадані
LABEL maintainer="your@email.com"

# Робоча директорія
WORKDIR /app

# Копіювання файлів
COPY requirements.txt .
COPY . .

# Встановлення залежностей
RUN pip install --no-cache-dir -r requirements.txt

# Відкриття порту
EXPOSE 8000

# Змінні середовища
ENV DEBUG=False

# Команда запуску
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
```

## Docker Compose
Приклад docker-compose.yml для веб-додатку з базою даних:

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/code
    environment:
      - DEBUG=True
    depends_on:
      - db

  db:
    image: postgres:13
    environment:
      POSTGRES_PASSWORD: example
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

### Команди для роботи з Compose:

```bash
docker-compose up -d
docker-compose down
docker-compose logs
```
## Корисні практики
### Оптимізація образів

- Використовуйте .dockerignore

- Об'єднуйте RUN команди

- Використовуйте багатоетапні збірки

### Безпека

- Не використовуйте root в контейнерах

- Оновлюйте базові образи

- Скануйте образи на вразливості

### Продуктивність

- Використовуйте томі для даних

- Обмежуйте ресурси контейнерів

- Використовуйте кешування при збірці

## Приклади використання
### Веб-додаток на Node.js
```bash
docker run -d -p 3000:3000 -v $(pwd):/app -w /app node:14 node app.js
```
### База даних MySQL
```bash
docker run -d -p 3306:3306 \
  -e MYSQL_ROOT_PASSWORD=secret \
  -v mysql_data:/var/lib/mysql \
  mysql:8.0
```

#### 📄 Ліцензія: Цей документ доступний на умовах MIT License