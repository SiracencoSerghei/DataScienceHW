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
- [Collaborative filtering](https://en.wikipedia.org/wiki/Collaborative_filtering)
- [Градієнтний спуск](https://uk.wikipedia.org/wiki/%D0%93%D1%80%D0%B0%D0%B4%D1%96%D1%94%D0%BD%D1%82%D0%BD%D0%B8%D0%B9_%D1%81%D0%BF%D1%83%D1%81%D0%BA)
- [Gradient descent](https://en.wikipedia.org/wiki/Gradient_descent)
- [MATRIX FACTORIZATION TECHNIQUES FOR RECOMMENDER SYSTEMS](https://datajobs.com/data-science-repo/Recommender-Systems-%5bNetflix%5d.pdf)
- [Multi-Objective Recommender System](https://www.kaggle.com/competitions/otto-recommender-system/discussion/376977)
- [Hybrid Recommendation System using Python](https://thecleverprogrammer.com/2023/06/05/hybrid-recommendation-system-using-python/)
- [Hybrid Recommender Systems: Beginner's Guide](https://marketsy.ai/blog/hybrid-recommender-systems-beginners-guide)
- [Відео](https://youtu.be/e-I_G9QhHTA?si=C-_0_YYMK_O5piya)
- [LightFM](https://making.lyst.com/lightfm/docs/home.html)

📌 **Бажаємо успіхів у роботі!**
