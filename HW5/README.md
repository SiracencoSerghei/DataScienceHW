# 🏠 Домашнє завдання

В цьому домашньому завданні ви потренуєтесь виконувати **тестове завдання** для влаштування на роботу.

### 📌 Завдання  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;              --> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;          📌 [Рішення]()

За даними **акселерометра** з мобільного телефону потрібно **класифікувати**, якою діяльністю займається людина:

- 🚶 **Йде**
- 🏃 **Біжить**
- 🏋️ **Стоїть**
- 🏞️ **Йде по сходах**


<p>📥 Датасет можна знайти за <a href="https://drive.google.com/file/d/1nzrtQpfaHL0OgJ_eXzA7VuEj7XotrSWO/view">посиланням</a></p>

---

## 🛠 Інструкція

1️⃣ Використайте **алгоритми**:

- **SVM (Support Vector Machine)**
- **Випадковий ліс (Random Forest)**
  з бібліотеки **scikit-learn**.

2️⃣ Використайте **показники з акселерометра** як характеристики.

- Щоб покращити результати, **розрахуйте часові ознаки** (*time domain features*).
<p> Більше інформації про ці характеристики описано в <a href='https://drive.google.com/file/d/1-18YEmp0YjV3hN9iI8J1i_FWd55HFwOK/view'>`даній статті`</a></p>

3️⃣ **Порівняйте результати** роботи обох алгоритмів:

- **На різних фічах**
- **Між різними моделями**

4️⃣ Використайте **метод `classification_report`** для порівняння.

---

## ❌ Що **НЕ** приймається?

🔴 **Порівняння моделей лише за однією метрикою**, наприклад, **Accuracy**, не приймається.

---

## ✅ Формат виконання

📌 Домашнє завдання має бути виконане у **Jupyter Notebook або Google Colab**.
📌 Фінальний файл **`.ipynb`** повинен бути **задеплоєний на GitHub**.

## 🔗 Корисні матеріали

📖 [Документація scikit-learn](https://scikit-learn.org/stable/) – Офіційний сайт бібліотеки

📖 [Методи класифікації](https://www.ibm.com/think/topics/classification-models#:~:text=Classification%20models%20are%20a%20type%20of%20machine%20learning%20model%20that,according%20to%20those%20learned%20characteristics.) – Основи класифікаційних алгоритмів

📖 [Методи класифікації](https://www.datacamp.com/blog/classification-machine-learning) – Основи класифікаційних алгоритмів

📖 [Метод опорних векторів](https://uk.wikipedia.org/wiki/Метод_опорних_векторів)

📖 [Метод опорних векторів](https://www.dstu.dp.ua/Portal/Data/74/72/3st13-17.pdf?) - pdf

📖 [Стаття про часові ознаки (time domain features)](https://www.researchgate.net/figure/List-of-extracted-time-domain-features-from-each-window-size_tbl2_327523090)

📖 [Відео-лекція: &#34;Метод опорних векторів. Аналіз головних компонент&#34;](https://youtu.be/Jr7_Cg_REa4?si=OL4868fTxzfLG1QF) — онлайн-лекція, яка пояснює принципи роботи SVM та його застосування.

📖 [Побудуйте поверхню рішень дерев рішень, навчених на наборі даних райдужної оболонки](https://scikit-learn.org/stable/auto_examples/tree/plot_iris_dtc.html#sphx-glr-auto-examples-tree-plot-iris-dtc-py)

📖 [Розуміння структури дерева рішень](https://scikit-learn.org/stable/auto_examples/tree/plot_unveil_tree_structure.html#sphx-glr-auto-examples-tree-plot-unveil-tree-structure-py)

📖 [xgboost.readthedocs.io](https://xgboost.readthedocs.io/en/stable/)

📖 [lightgbm.readthedocs.io](https://lightgbm.readthedocs.io/en/stable/)

📖 [Examples](https://scikit-learn.org/stable/auto_examples/ensemble/index.html)

📖 [калькулятор](https://www.wolframalpha.com/)

[KDNuggets: ](https://www.kdnuggets.com/5-step-blueprint-to-your-next-data-science-problem)

📖 [Data Camp: ](https://www.datacamp.com/blog/data-science-use-cases-guide)

📖 [10 Steps: ](https://towardsdatascience.com/10-steps-to-pass-the-data-science-take-home-task-c5a696679526/)

📖 [Notebook Template: ](https://medium.com/@jacowp357/12-steps-towards-implementing-a-data-science-solution-d2ce196f22c1)

---

🚀 **Успіхів у виконанні завдання!**
