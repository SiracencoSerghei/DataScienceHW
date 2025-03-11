# 🏆 Домашнє завдання: Розпізнавання рукописних цифр ✍️🔢

🎯 **Мета завдання:**  
Розробити та навчити нейронну мережу, яка зможе розпізнавати рукописні цифри.

Завантажте в гугл колаб [цей](https://drive.google.com/file/d/10-gPf1AeEKXKOlZq9ItbKRo8gtmtNiDV/view) ноутбук. 

📌 **Що потрібно зробити?**  
✅ Заповнити пропуски у коді.  
✅ Навчити нейронну мережу.  
✅ Побудувати графіки навчання. 📊  
✅ Оцінити втрати моделі. ⚠️  
✅ Протестувати мережу на тестових даних. 🧪  
✅ Вивести **метрики якості** для кожного класу, використовуючи [`classification_report`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html).  
✅ **Зробити висновки** про якість навченої моделі. 📝  


# Створення та навчання нейронної мережі на датасеті MNIST

## 1. Теоретична частина

### 1.1. Нейронна мережа
Нейронна мережа — це математична модель, яка імітує роботу людського мозку. Вона складається з шарів:

- **Вхідний шар**: отримує вхідні дані (наприклад, пікселі зображення).
- **Приховані шари**: обробляють дані за допомогою ваг та функцій активації.
- **Вихідний шар**: повертає результат (наприклад, клас зображення).

### 1.2. Функції активації

- **Сигмоїда**:  
  $$\sigma(x) = \frac{1}{1 + e^{-x}}$$  
  Використовується у прихованих шарах. Перетворює вхідні дані у діапазон [0, 1].

- **Softmax**:  
  $$\text{softmax}(x_i) = \frac{e^{x_i}}{\sum_j e^{x_j}}$$  
  Використовується у вихідному шарі для багатокласової класифікації. Перетворює вихідні значення у ймовірності.

### 1.3. Функція втрат

- **Крос-ентропія**:  
  $$L = -\sum_i y_i \log(\hat{y}_i)$$  
  - $y_i$ — правильна мітка (one-hot encoding).
  - $\hat{y}_i$ — передбачення моделі.  
  Використовується для оцінки помилки моделі.

### 1.4. Оптимізація

- **Стохастичний градієнтний спуск (SGD)**:  
  Оновлює ваги мережі:  
  $$w = w - \eta \nabla L$$  
  - $\eta$ — швидкість навчання.
  - $\nabla L$ — градієнт функції втрат.

## 2. Практична частина

### 2.1. Підготовка даних

- **Датасет MNIST**:
  Зображення рукописних цифр розміром 28x28 пікселів.

- **Нормалізація**: значення пікселів масштабуються до [0, 1].
- **Перетворення**: матриця 28x28 розгортається у вектор з 784 елементів.

```python
# Завантаження даних
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Нормалізація та перетворення
x_train = x_train.reshape([-1, 784]) / 255.0
x_test = x_test.reshape([-1, 784]) / 255.0
```

## 2.2. Архітектура мережі

### Шари:
- Вхідний шар: 784 нейрони (один на кожен піксель).
- Прихований шар 1: 128 нейронів з сигмоїдою.
- Прихований шар 2: 256 нейронів з сигмоїдою.
- Вихідний шар: 10 нейронів з softmax (один на кожну цифру).

```python
class DenseLayer(tf.Module):
    def __init__(self, in_features, out_features):
        self.w = tf.Variable(tf.random.normal([in_features, out_features]))
        self.b = tf.Variable(tf.zeros([out_features]))

    def __call__(self, x, activation=0):
        y = tf.matmul(x, self.w) + self.b
        return tf.nn.sigmoid(y) if activation == 0 else tf.nn.softmax(y)

class NN(tf.Module):
    def __init__(self):
        self.layer1 = DenseLayer(784, 128)
        self.layer2 = DenseLayer(128, 256)
        self.output_layer = DenseLayer(256, 10)

    def __call__(self, x):
        x = self.layer1(x, activation=0)
        x = self.layer2(x, activation=0)
        return self.output_layer(x, activation=1)
```

## 2.3. Навчання мережі

### Функція втрат: крос-ентропія.
### Оптимізація: SGD.

```python
def train(neural_net, input_x, output_y):
    optimizer = tf.optimizers.SGD(learning_rate)
    with tf.GradientTape() as g:
        pred = neural_net(input_x)
        loss = cross_entropy(pred, output_y)
    gradients = g.gradient(loss, neural_net.trainable_variables)
    optimizer.apply_gradients(zip(gradients, neural_net.trainable_variables))
```
## 2.4. Оцінка моделі

### Точність: частка правильних передбачень.

```python
def accuracy(y_pred, y_true):
    correct = tf.equal(tf.argmax(y_pred, 1), tf.cast(y_true, tf.int64))
    return tf.reduce_mean(tf.cast(correct, tf.float32))
```

## Висновки

- Нейронна мережа навчається класифікувати цифри з високою точністю.
- Помилки можуть виникати через схожість цифр (наприклад, 3 та 8).

### Для покращення результатів можна:
- Збільшити кількість епох.
- Використовувати інші функції активації (наприклад, ReLU).
- Застосувати регуляризацію (наприклад, dropout).


---
# 🔗 **Корисні ресурси:**
---

1. **TensorFlow & Keras:**
   - Офіційні туторіали для створення нейронних мереж:
     - [TensorFlow Tutorials](https://www.tensorflow.org/tutorials)
     - [Keras Documentation](https://keras.io/)
     - [Автоматичне диференціювання в tensorflow](https://www.tensorflow.org/guide/intro_to_graphs)
     - [Реалізація моделей](https://www.tensorflow.org/guide/intro_to_modules)
     - [Навчання моделей](https://www.tensorflow.org/guide/basic_training_loops)
     - [Обчислювальні графи](https://www.tensorflow.org/guide/intro_to_graphs)
     - [Корисні приклади](https://github.com/tensorflow/docs)
   
2. **Scikit-learn для метрик якості:**
   - Для отримання метрик якості моделі, зокрема **classification_report**:
     - [classification_report в Scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html)

3. **MNIST Dataset (дані для розпізнавання цифр):**
   - Один з найбільш відомих датасетів для завдань з розпізнавання цифр:
     - [MNIST Dataset на TensorFlow](https://www.tensorflow.org/datasets/community_catalog/huggingface/mnist)
     - [MNIST Dataset на Scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html)

4. **Загальні ресурси для нейронних мереж:**
   - [Deep Learning Specialization на Coursera](https://www.coursera.org/specializations/deep-learning)
   - [Прості приклади для нейронних мереж на TensorFlow](https://www.tensorflow.org/tutorials/keras/classification)
   - [ PyTorch](https://pytorch.org/get-started/locally/)
   - [Візуалізатор навчання нейронних мереж.](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=4,2&seed=0.11967&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false)
   - [Sigmoid function](https://machinelearningmastery.com/a-gentle-introduction-to-sigmoid-function/)

5. **Інструменти для візуалізації:**
   - [Matplotlib Documentation](https://matplotlib.org/stable/contents.html) – для побудови графіків навчання.
   - [Seaborn Documentation](https://seaborn.pydata.org/) – для створення візуалізацій та графіків.


🚀 **Успіхів!** 🚀  
