
# Streamlit — Короткий конспект з прикладами коду

## 1. Вступ
Streamlit — це Python-фреймворк для швидкого створення інтерактивних веб-додатків для Data Science та Machine Learning без знання HTML/CSS/JS.

---

## 2. Встановлення та запуск
```bash
pip install streamlit
streamlit hello  # демо-додаток
streamlit run app.py  # запуск свого коду
```

---

## 3. Основні віджети
```python
import streamlit as st

st.title("Приклад застосунку")
st.write("Привіт, Streamlit!")

# Слайдер
age = st.slider("Вік", 0, 100, 25)
st.write("Ваш вік:", age)

# Вибір зі списку
option = st.selectbox("Виберіть опцію", ["A", "B", "C"])
st.write("Ви вибрали:", option)

# Чекбокс
if st.checkbox("Показати текст"):
    st.write("Текст показано!")
```

---

## 4. Завантаження файлів
```python
uploaded_file = st.file_uploader("Завантажте файл", type=["csv", "png", "jpg"])

if uploaded_file is not None:
    st.write("Ім'я файлу:", uploaded_file.name)
```

---

## 5. Відображення графіків та зображень
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig)

from PIL import Image
image = Image.open("example.png")
st.image(image, caption="Приклад зображення", use_column_width=True)
```

---

## 6. Інтеграція ML-моделей
```python
import tensorflow as tf
from PIL import Image
import numpy as np

model = tf.keras.models.load_model("model.h5")

uploaded_file = st.file_uploader("Завантажте зображення", type=["jpg", "png"])
if uploaded_file:
    img = Image.open(uploaded_file).resize((224, 224))
    img_array = np.array(img) / 255.0
    pred = model.predict(np.expand_dims(img_array, axis=0))
    st.write("Результат передбачення:", pred)
```

---

## 7. Меню та навігація (streamlit-option-menu)
```python
from streamlit_option_menu import option_menu

selected = option_menu(
    menu_title=None,
    options=["Home", "About", "Contact"],
    icons=["house", "info-circle", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

if selected == "Home":
    st.title("Головна сторінка")
elif selected == "About":
    st.title("Про нас")
```

---

## 8. Авторизація через SQLite
```python
import sqlite3, hashlib

def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT)')

# Додавання користувача
c.execute('INSERT INTO users(username, password) VALUES (?, ?)', ("admin", make_hashes("1234")))
conn.commit()
```

---

## 9. Деплой на Streamlit Cloud
1. Зробити репозиторій на GitHub з вашим кодом.
2. Зайти на [Streamlit Cloud](https://streamlit.io/cloud).
3. Підключити GitHub репозиторій.
4. Обрати `app.py` як головний файл.
5. Запустити застосунок.
