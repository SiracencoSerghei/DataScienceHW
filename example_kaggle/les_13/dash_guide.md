# Dash — Розширений конспект з прикладами коду та поясненнями

## 1. Вступ
Dash — це Python-фреймворк від Plotly для створення аналітичних веб-додатків з інтерактивними графіками.  
Він дозволяє створювати веб-інтерфейси для аналізу даних без використання HTML, CSS чи JavaScript.

---

## 2. Встановлення та запуск
Встановлюємо Dash і бібліотеку Plotly для побудови графіків:
```bash
pip install dash plotly
```
Запуск застосунку:
```bash
python app.py
```
За замовчуванням Dash запустить сервер на `http://127.0.0.1:8050/`.

---

## 3. Базовий приклад
```python
import dash
from dash import html

app = dash.Dash(__name__)  # створюємо застосунок

# Створюємо розмітку сторінки
app.layout = html.Div([
    html.H1("Привіт, Dash!"),
    html.P("Мій перший веб-застосунок")
])

if __name__ == '__main__':
    app.run_server(debug=True)  # запускаємо сервер
```
**Пояснення:**
- `dash.Dash()` створює екземпляр застосунку.
- `app.layout` описує HTML-компоненти сторінки.
- `html.Div`, `html.H1`, `html.P` — це елементи, що відповідають HTML-тегам `<div>`, `<h1>`, `<p>`.

---

## 4. Використання компонентів
```python
from dash import dcc, html

app.layout = html.Div([
    html.H1("Приклад компонентів"),
    dcc.Input(id='input-text', type='text', value=''),
    html.Div(id='output-text')
])
```
**Пояснення:**
- `dcc.Input` — поле вводу тексту.
- `html.Div(id='output-text')` — контейнер для виводу результату.

---

## 5. Колбеки (Callbacks)
```python
from dash.dependencies import Input, Output

@app.callback(
    Output('output-text', 'children'),
    Input('input-text', 'value')
)
def update_text(value):
    return f"Ви ввели: {value}"
```
**Пояснення:**
- `@app.callback` дозволяє зв'язати вхідні дані (`Input`) з вихідними (`Output`).
- Тут зміна значення в полі вводу автоматично змінює текст у `output-text`.

---

## 6. Інтерактивні графіки (Plotly)
```python
import plotly.express as px
import pandas as pd

df = px.data.iris()  # вбудований датасет Iris

app.layout = html.Div([
    dcc.Graph(
        id='scatter-plot',
        figure=px.scatter(df, x='sepal_width', y='sepal_length', color='species')
    )
])
```
**Пояснення:**
- `dcc.Graph` відображає інтерактивний графік.
- `px.scatter()` створює діаграму розсіювання з бібліотеки Plotly.

---

## 7. Завантаження файлів
```python
dcc.Upload(
    id='upload-data',
    children=html.Div(['Перетягніть файл або ', html.A('Оберіть файл')]),
    multiple=False
)
```
**Пояснення:**
- `dcc.Upload` дозволяє завантажувати файли у веб-додаток.
- `multiple=False` означає, що можна завантажити тільки один файл.

---

## 8. Dash з кількома сторінками
```python
app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.layout = html.Div([dcc.Location(id='url'), html.Div(id='page-content')])
```
**Пояснення:**
- `dcc.Location` відстежує зміну URL.
- `page-content` оновлюється залежно від маршруту.

---

## 9. Деплой на Heroku
1. Створити `requirements.txt` з бібліотеками.
2. Створити `Procfile`:
```
web: gunicorn app:app.server
```
3. Завантажити код у GitHub.
4. Підключити репозиторій до Heroku.
5. Розгорнути застосунок.

---

## 10. Корисні ресурси
- [Документація Dash](https://dash.plotly.com/)
- [Приклади Plotly](https://plotly.com/python/)
