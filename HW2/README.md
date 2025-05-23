# Домашнє завдання


Не турбуйтеся, якщо у вас не буде все одразу виходити. Робота будь-якого дата саєнтіста тісно пов'язана з пошуком та дослідженнями, тому дуже важливо навчитися шукати потрібну інформацію та адаптувати її під свої потреби. Також, з будь-якими питаннями ви можете звертатися до ментора.



## Частина перша: Знайомство з Pandas.

​

Прочитайте дані за допомогою методу read_html з таблиці ["Коефіцієнт народжуваності в регіонах України (1950—2019)"](https://uk.wikipedia.org/wiki/%D0%9D%D0%B0%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%BD%D1%8F_%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D0%B8)

Необхідно виконати:


    Вивести перші рядки таблиці за допомогою методу head
    Визначте кількість рядків та стовпців у датафреймі (атрибут shape)
    Замініть у таблиці значення "—" на значення NaN
    Визначте типи всіх стовпців за допомогою dataframe.dtypes
    Замініть типи нечислових колонок на числові. Підказка - це колонки, де знаходився символ "—"
    Порахуйте, яка частка пропусків міститься в кожній колонці (використовуйте методи isnull та sum)
    Видаліть з таблиці дані по всій країні, останній рядок таблиці
    Замініть відсутні дані в стовпцях середніми значеннями цих стовпців (метод fillna)
    Отримайте список регіонів, де рівень народжуваності у 2019 році був вищим за середній по Україні
    У якому регіоні була найвища народжуваність у 2014 році?
    Побудуйте стовпчикову діаграму народжуваності по регіонах у 2019 році


Робота здається у вигляді Jupyter файлу Hw2.1.ipynb



## Частина друга: Аналіз файлів

​

Проведіть аналіз файлу 2017_jun_final.csv. Файл містить результати опитування розробників у червні 2017 року.


Необхідно виконати:


    Прочитайте файл 2017_jun_final.csv за допомогою методу read_csv
    Прочитайте отриману таблицю, використовуючи метод head
    Визначте розмір таблиці за допомогою методу shape
    Визначте типи всіх стовпців за допомогою dataframe.dtypes
    Порахуйте, яка частка пропусків міститься в кожній колонці (використовуйте методи isnull та sum)
    Видаліть усі стовпці з пропусками, крім стовпця "Мова програмування"
    Знову порахуйте, яка частка пропусків міститься в кожній колонці і переконайтеся, що залишився тільки стовпець "Мова.програмування"
    Видаліть усі рядки у вихідній таблиці за допомогою методу dropna
    Визначте новий розмір таблиці за допомогою методу shape
    Створіть нову таблицю python_data, в якій будуть тільки рядки зі спеціалістами, які вказали мову програмування Python
    Визначте розмір таблиці python_data за допомогою методу shape
    Використовуючи метод groupby, виконайте групування за стовпчиком "Посада"
    Створіть новий DataFrame, де для згрупованих даних за стовпчиком "Посада", виконайте агрегацію даних за допомогою методу agg і знайдіть мінімальне та максимальне значення у стовпчику "Зарплата.в.місяць"
    Створіть функцію fill_avg_salary, яка повертатиме середнє значення заробітної плати на місяць. Використовуйте її для методу apply та створіть новий стовпчик "avg"
    Створіть описову статистику за допомогою методу describe для нового стовпчика.
    Збережіть отриману таблицю в CSV файл


Робота здається у вигляді Jupyter файлу Hw2.2.ipynb



## Частина третя: Аналіз датасет c Kaggle.com

​

У цій частині домашньої роботи ми ще більше заглибимося в бібліотеку pandas та розглянемо просунутіші функції.


Для цієї вправи ми використовуємо дані за Топ-50 рейтингом книг, що найбільше продаються на Amazon за 11 років (з 2009 по 2019). Датасет знаходиться у відкритому доступі на Kaggle.com. Завантажте файл csv за посиланням і перемістіть його в ту саму директорію, де знаходиться ваш робочий ноутбук (для зручності). Після цього переходьте до завдання


Для виконання цієї частини домашнього завдання потрібно буде не тільки написати код, а й відповісти на супутні запитання. Там, де ви побачите виділений жирним шрифтом напис відповідь: потрібно буде вставити питання у файл і відповідь на нього.


Наприклад:


Яка бібліотека використовується для роботи з датафреймами у python? Відповідь: pandas


Необхідно виконати:


    Прочитайте csv файл (використовуйте функцію read_csv)
    Виведіть перші п'ять рядків (використовується функція head)
    Виведіть розміри датасету (використовуйте атрибут shape)
    Відповідь: Про скільки книг зберігає дані датасет?


Для кожної з книг доступні 7 змінних (колонок). Давайте розглянемо їх детальніше:


Name - назва книги

Author - автор

User Rating - рейтинг (за 5-бальною шкалою)

Reviews - кількість відгуків

Price - ціна (у доларах станом на 2020 рік)

Year - рік, коли книга потрапила до рейтингу Топ-50

Genre - жанр


Для спрощення подальшої роботи давайте трохи підправимо назви змінних. Як бачите, тут усі назви починаються з великої літери, а одна - навіть містить пробіл. Це дуже небажано і може бути досить незручним. Давайте змінимо регістр на малий, а пробіл замінимо на нижнє підкреслення (snake_style). А заразом і вивчимо корисний атрибут датафрейму: columns (можна просто присвоїти список нових імен цьому атрибуту)


df.columns = ['name', 'author', 'user_rating', 'reviews', 'price', 'year', 'genre']



Первинне дослідження даних


    Перевірте, чи у всіх рядків вистачає даних: виведіть кількість пропусків (na) у кожному зі стовпців (використовуйте функції isna та sum)
    Відповідь: Чи є в якихось змінних пропуски? (Так / ні)
    Перевірте, які є унікальні значення в колонці genre (використовуйте функцію unique)
    Відповідь: Які є унікальні жанри?
    Тепер подивіться на розподіл цін: побудуйте діаграму (використовуйте kind='hist')
    Визначте, яка ціна у нас максимальна, мінімальна, середня, медіанна (використовуйте функції max, min, mean, median)
    Відповідь: Максимальна ціна?
    Відповідь: Мінімальна ціна?
    Відповідь: Середня ціна?
    Відповідь: Медіанна ціна?



Пошук та сортування даних

​

    Відповідь: Який рейтинг у датасеті найвищий? Відповідь:
    Відповідь: Скільки книг мають такий рейтинг? Відповідь:
    Відповідь: Яка книга має найбільше відгуків? Відповідь:
    Відповідь: З тих книг, що потрапили до Топ-50 у 2015 році, яка книга найдорожча (можна використати проміжний датафрейм)? Відповідь:
    Відповідь: Скільки книг жанру Fiction потрапили до Топ-50 у 2010 році (використовуйте &)? Відповідь:
    Відповідь: Скільки книг з рейтингом 4.9 потрапило до рейтингу у 2010 та 2011 роках (використовуйте | або функцію isin)? Відповідь:
    І насамкінець, давайте відсортуємо за зростанням ціни всі книги, які потрапили до рейтингу в 2015 році і коштують дешевше за 8 доларів (використовуйте функцію sort_values).
    Відповідь: Яка книга остання у відсортованому списку? Відповідь:



Агрегування даних та з'єднання таблиць

​

Остання секція цього домашнього завдання включає просунутіші функції. Але не хвилюйтеся, pandas робить усі операції простими та зрозумілими.


    Для початку давайте подивимося на максимальну та мінімальну ціни для кожного з жанрів (використовуйте функції groupby та agg, для підрахунку мінімальних та максимальних значень використовуйте max та min). Не беріть усі стовпці, виберіть тільки потрібні вам
    Відповідь: Максимальна ціна для жанру Fiction: Відповідь
    Відповідь: Мінімальна ціна для жанру Fiction: Відповідь
    Відповідь: Максимальна ціна для жанру Non Fiction: Відповідь
    Відповідь: Мінімальна ціна для жанру Non Fiction: Відповідь
    Тепер створіть новий датафрейм, який вміщатиме кількість книг для кожного з авторів (використовуйте функції groupby та agg, для підрахунку кількості використовуйте count). Не беріть усі стовпці, виберете тільки потрібні
    Відповідь: Якої розмірності вийшла таблиця? Відповідь:
    Відповідь: Який автор має найбільше книг? Відповідь:
    Відповідь: Скільки книг цього автора? Відповідь:
    Тепер створіть другий датафрейм, який буде вміщати середній рейтинг для кожного автора (використовуйте функції groupby та agg, для підрахунку середнього значення використовуйте mean). Не беріть усі стовпці, виберете тільки потрібні
    Відповідь: У якого автора середній рейтинг мінімальний? Відповідь:
    Відповідь: Який у цього автора середній рейтинг? Відповідь:
    З'єднайте останні два датафрейми так, щоб для кожного автора було видно кількість книг та середній рейтинг (Використовуйте функцію concat з параметром axis=1). Збережіть результат у змінну
    Відсортуйте датафрейм за зростаючою кількістю книг та зростаючим рейтингом (використовуйте функцію sort_values)
    Відповідь: Який автор перший у списку?


Робота здається у вигляді Jupyter файлу Hw2.3.ipynb



Візуалізація

​

Для кожного з попередніх завдань:


    Hw2.1.ipynb
    Hw2.2.ipynb
    Hw2.3.ipynb


додайте від 3 до 5 графіків функцій різного типу на ваш вибір. Задайте графікам оформлення, щоб кожен графік у своїй домашній роботі чимось відрізнявся і не був схожим на інші. Можна використовувати як matplotlib, так і seaborn.


Не забудьте в Jupyter файл додати директиву %matplotlib inline, щоб графіки будувалися всередині документа.


Дз повинно бути виконано у Jupyter Nootebook,(або Google Colab) і задеплоїне на Гітхаб у вигляді файлу .ipynb
