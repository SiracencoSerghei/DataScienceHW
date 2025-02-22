# Домашнє завдання модуля: Рекомендаційні системи

На цьому тижні ми вивчили, як працюють рекомендаційні системи. Пропонуємо вам познайомитися з бібліотекою **Surprise**, яка є доповненням до знайомої нам бібліотеки **scikit-learn** для тренування моделей рекомендаційних систем.

## Завдання

1. Візьміть датасет **MovieLens** і побудуйте модель **[матричної факторизації](https://en.wikipedia.org/wiki/Matrix_factorization_(recommender_systems))**.  
   У бібліотеці Surprise цей метод має назву **[SVD]()**.  
   
2. Підберіть найкращі параметри за допомогою **крос-валідації**.

3. Поекспериментуйте з іншими алгоритмами розрахунків (**SVD++, NMF**)  
   та оберіть той, який буде оптимальним.

📌 **Підказка**: як саме побудувати дану модель, ви знайдете в [документації Surprise](https://surprise.readthedocs.io/en/stable/getting_started.html#getting-started).

---

## Додаткове завдання 🌟

Для глибшого розуміння алгоритму пропонуємо реалізувати **алгоритм колабораційної фільтрації з нуля**.  

Для цього можна скористатися домашньою роботою з **[3-го модуля](https://github.com/SiracencoSerghei/DataScienceHW/tree/main/HW3)**.  
Якщо модифікувати функцію втрат та розрахунок градієнтів,  
то можна побудувати **алгоритм матричної факторизації**.

[Тут](https://colab.research.google.com/drive/1biZdo4pc_Kkm-JvZsuadqDVphfUu1sGk?usp=sharing) ви можете побачити формули та завантаження датасету. А ось посилання на [назви фільмів](https://drive.google.com/file/d/12XeO4KXQfbvvTdLFbkYA-BeXzhlNnnuo/view) та на [рейтинги](https://drive.google.com/file/d/17V9OhXeZH9Wv17Nkh-Tqxa8svEmRZcIp/view).


🔗 **Корисні ресурси**:  
- [Формули та завантаження датасету](https://grouplens.org/datasets/movielens/)  
- [Назви фільмів та рейтинги](https://files.grouplens.org/datasets/movielens/ml-latest-small.zip)

📌 **Бажаємо успіхів у роботі!**
