# Веб-застосунок для візуалізації роботи нейронної мережі (Streamlit)

## Опис завдання

Мета проєкту — створити веб-застосунок для візуалізації роботи навченої нейронної мережі з класифікації зображень.
Це домашнє завдання є продовженням попереднього модуля **"Згорткові нейронні мережі"**.

---

## Функціонал застосунку

1. **Завантаження зображення**Користувач може завантажити зображення для класифікації через інтерфейс веб-додатка.
2. **Відображення вхідного зображення**Завантажене зображення відображається на сторінці.
3. **Вивід графіків функції втрат і точності**Показуються графіки **Loss** та **Accuracy** для моделі, отримані під час навчання.
4. **Відображення результатів класифікації**

   - Ймовірності для кожного класу (у вигляді таблиці або стовпчикової діаграми).
   - Передбачений клас.
5. **Вибір моделі**Інтерфейс дозволяє перемикатися між:

   - Згортковою нейронною мережею з Частини 1.
   - Моделлю на основі VGG16 з Частини 2.

---

## Використані технології

- **Python 3.9+**
- **TensorFlow / Keras** — для роботи з моделями нейронних мереж.
- **Matplotlib / Plotly** — для побудови графіків.
- **Pandas / NumPy** — для обробки даних.
- **Streamlit** або **Dash** — для побудови веб-інтерфейсу.

---

## Структура проєкту

```
project/
│── models/
│   ├── cnn_model.h5         # Модель з Частини 1
│   ├── vgg16_model.h5       # Модель з Частини 2
│── images/
│   ├── example.jpg          # Приклад зображення
│── app.py                   # Основний файл застосунку
│── utils.py                 # Допоміжні функції
│── requirements.txt         # Необхідні бібліотеки
│── README.md                # Документація
```

---

## Як запустити

1. Клонувати репозиторій:

```bash
git clone https://github.com/username/project.git
cd project
```

2. Встановити залежності:

```bash
pip install -r requirements.txt
```

3. Запустити застосунок:

```bash
streamlit run app.py
```

або

```bash
python app.py
```

---

## Приклад роботи

- Завантажуємо зображення.
- Вибираємо модель.
- Отримуємо:
  - Передбачений клас.
  - Ймовірності для кожного класу.
  - Графіки Loss та Accuracy.

---

## Корисні ресурси

### Статті:

- [Як працювати зі Streamlit для Data Science](https://blog.streamlit.io/how-to-master-streamlit-for-data-science/)
- [Приклад створення застосунку на Streamlit](https://medium.com/crossml/streamlit-2256000541ad)
- [Створення застосунків на Streamlit з TensorFlow](https://towardsdatascience.com/build-an-app-to-synthesize-photorealistic-faces-using-tensorflow-and-streamlit-dd2545828021)
- [Приклад бізнес-аналітики зі Streamlit](https://dev.to/ivancasillaaa/creating-a-sales-analysis-application-with-streamlit-a-practical-approach-to-business-intelligence-1c4l)
- [Дашборд у Streamlit](https://dev.to/fiorelamilady/building-and-deploying-a-dashboard-in-the-cloud-with-streamlit-and-python-4hm2)
- [Рекомендаційна система зі Streamlit](https://dev.to/tanmaypatil123/building-a-powerful-recommendation-system-with-palm-2-model-and-streamlit-a-step-by-step-guide-4n64)
- [Деплой застосунків зі Streamlit](https://dev.to/surendraredd/how-to-deploy-streamlitapp-2p53)

### Відео:

- [Streamlit для початківців](https://www.youtube.com/watch?v=e_OPmGjkAVs)
- [Streamlit офіційний плейлист](https://www.youtube.com/watch?v=_9WiB2PDO7k&list=PLJ39kWiJXSixyRMcn3lrbv8xI8ZZoYNZU)
- [Приклади з ML](https://www.youtube.com/watch?v=UN4DaSAZel4&list=PLuU3eVwK0I9PT48ZBYAHdKPFazhXg76h5)
- [Створення застосунку на Streamlit](https://www.youtube.com/watch?v=KDcz2mF3Yuk&list=PLtqF5YXg7GLkn2FNYA20y4D3DZKotdtmo)
- [Streamlit Crash Course](https://www.youtube.com/watch?v=JwSS70SZdyM)

# Веб-застосунок для візуалізації роботи нейронної мережі (Dash)

## Опис завдання

Мета проєкту — створити веб-застосунок для візуалізації роботи навченої нейронної мережі з класифікації зображень.
Це домашнє завдання є продовженням попереднього модуля **"Згорткові нейронні мережі"**.

---

## Функціонал застосунку

1. **Завантаження зображення**Користувач може завантажити зображення для класифікації через інтерфейс веб-додатка.
2. **Відображення вхідного зображення**Завантажене зображення відображається на сторінці.
3. **Вивід графіків функції втрат і точності**Показуються графіки **Loss** та **Accuracy** для моделі, отримані під час навчання.
4. **Відображення результатів класифікації**

   - Ймовірності для кожного класу (у вигляді таблиці або стовпчикової діаграми).
   - Передбачений клас.
5. **Вибір моделі**Інтерфейс дозволяє перемикатися між:

   - Згортковою нейронною мережею з Частини 1.
   - Моделлю на основі VGG16 з Частини 2.

---

## Використані технології

- **Python 3.9+**
- **TensorFlow / Keras** — для роботи з моделями нейронних мереж.
- **Matplotlib / Plotly** — для побудови графіків.
- **Pandas / NumPy** — для обробки даних.
- **Dash** — для побудови веб-інтерфейсу.

---

## Структура проєкту

```
project/
│── models/
│   ├── cnn_model.h5         # Модель з Частини 1
│   ├── vgg16_model.h5       # Модель з Частини 2
│── images/
│   ├── example.jpg          # Приклад зображення
│── app.py                   # Основний файл застосунку (Dash)
│── utils.py                 # Допоміжні функції
│── requirements.txt         # Необхідні бібліотеки
│── README.md                # Документація
```

---

## Як запустити

1. Клонувати репозиторій:

```bash
git clone https://github.com/username/project.git
cd project
```

2. Встановити залежності:

```bash
pip install -r requirements.txt
```

3. Запустити застосунок:

```bash
python app.py
```

4. Відкрити у браузері:

```
http://127.0.0.1:8050/
```

---

## Приклад роботи

- Завантажуємо зображення.
- Вибираємо модель.
- Отримуємо:
  - Передбачений клас.
  - Ймовірності для кожного класу.
  - Графіки Loss та Accuracy.

---

## Корисні ресурси по Dash

### Статті:

- [Офіційна документація Dash](https://dash.plotly.com/)
- [Вступ до Dash](https://towardsdatascience.com/getting-started-with-plotly-dash-9aa7d7b4e0f3)
- [Dash + Machine Learning приклад](https://towardsdatascience.com/building-interactive-machine-learning-tools-with-dash-236e159f8d46)
- [Інтерактивні графіки з Plotly та Dash](https://plotly.com/python/plotly-express/)

### Відео:

- [Dash Crash Course](https://www.youtube.com/watch?v=hSPmj7mK6ng)
- [Data Visualization з Dash](https://www.youtube.com/watch?v=GGL6U0k8WYA)
- [ML-додаток на Dash](https://www.youtube.com/watch?v=zG2JRuR2gUM)
