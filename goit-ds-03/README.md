# Домашнє завдання 3 — GoIT Data Science

## Завдання 1: CRUD-операції з MongoDB

Реалізовано скрипт `main.py`, який підключається до MongoDB (локально або через MongoDB Atlas) і дозволяє:

- Додати запис про кота
- Отримати всі записи
- Знайти кота за ім'ям
- Оновити вік кота
- Додати нову характеристику
- Видалити запис
- Видалити всі записи

### Запуск

```
poetry install
poetry shell  
```

```
 python3 run_mongo_container.py
```

```
python3 seed.py
```

```
python3 main.py
```
## Завдання 2: Скрапінг цитат

Скрапінг сайту http://quotes.toscrape.com для збереження:

- У `quotes.json` — цитати з усіх сторінок
- У `authors.json` — розгорнута інформація про кожного унікального автора

### Запуск

```
scrape_quotes.py
```

## 🔗 Корисні матеріали

## MongoDB

- [MongoDB Atlas Setup](https://www.mongodb.com/cloud/atlas)
- [PyMongo Documentation](https://pymongo.readthedocs.io/en/stable/)

## Скрапінг

- [BeautifulSoup Docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Documentation](https://requests.readthedocs.io/en/latest/)
- [quotes.toscrape.com](http://quotes.toscrape.com)

## GitHub

- [Як завантажити проєкт на GitHub](https://docs.github.com/en/get-started)





 