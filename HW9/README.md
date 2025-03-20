# Домашнє завдання

## Опис завдання
В якості домашнього завдання вам пропонується створити нейронну мережу за допомогою механізмів **Keras**, яка буде класифікувати товари із датасету **Fashion MNIST**.

Вам належить запропонувати **власну архітектуру мережі**. Точність найнаївнішої, але адекватної нейромережі становить приблизно **91%**. Точність вашої моделі повинна бути **не нижчою** за цей показник.  

## Основні параметри для експериментів
Щоб досягти високої точності, вам потрібно протестувати різні **гіперпараметри** мережі, а саме:

- **Кількість шарів**
- **Кількість нейронів**
- **Функції активації**
- **Кількість епох**
- **Розмір батчу**
- **Вибір оптимізатора**
- **Різні техніки регуляризації** (dropout, batch normalization, Adam і т.д.)

## Покращення навчання
Використайте вивчені **техніки виявлення проблем навчання** нейронної мережі та експериментуйте зі способами їх подолання.

## Фінальне рішення
Оформіть своє рішення у вигляді **окремого Jupyter Notebook** із поясненнями щодо вибору архітектури та параметрів моделі.

## Корисні ресурси

### 1. **Документація та офіційні гайди**
- [Keras Documentation](https://keras.io/)  
  Офіційна документація Keras містить детальний опис усіх функцій, класів та методів, які можна використовувати для побудови моделей.

- [TensorFlow Guide](https://www.tensorflow.org/guide)  
  Офіційний гайд від TensorFlow, який охоплює всі аспекти роботи з Keras та TensorFlow.

- [Fashion MNIST Dataset](https://github.com/zalandoresearch/fashion-mnist)  
  Офіційний репозиторій датасету Fashion MNIST, де можна знайти опис даних, приклади коду та додаткові матеріали.

### 2. **Практичні туторіали**
- [TensorFlow Tutorials](https://www.tensorflow.org/tutorials)  
  Колекція туторіалів від TensorFlow, які охоплюють різні аспекти роботи з нейронними мережами, включаючи класифікацію зображень.

- [Keras Tutorial for Beginners](https://www.datacamp.com/tutorial/keras-tutorial-deep-learning-in-python)  
  Туторіал для початківців, який пояснює, як створювати моделі за допомогою Keras.

- [Fashion MNIST Classification with Keras](https://www.tensorflow.org/tutorials/keras/classification)  
  Туторіал від TensorFlow, який показує, як класифікувати Fashion MNIST за допомогою Keras.

### 3. **Теорія та пояснення**
- [Understanding the Bias-Variance Tradeoff](https://towardsdatascience.com/understanding-the-bias-variance-tradeoff-165e6942b229)  
  Стаття, яка пояснює, що таке bias-variance tradeoff і як це впливає на навчання моделей.

- [Regularization in Neural Networks](https://towardsdatascience.com/regularization-in-neural-networks-3a848d5d3a72)  
  Детальний огляд методів регуляризації, таких як dropout, batch normalization та L2 regularization.

- [Activation Functions in Neural Networks](https://towardsdatascience.com/activation-functions-in-neural-networks-83ff7f46a6bd)  
  Стаття, яка пояснює різні функції активації та їх вплив на навчання нейронних мереж.

### 4. **Оптимізація моделей**
- [A Comprehensive Guide to Fine-Tuning Deep Learning Models](https://towardsdatascience.com/a-comprehensive-guide-to-fine-tuning-deep-learning-models-in-keras-4c4c1d0f3e1a)  
  Гайд, який пояснює, як налаштовувати гіперпараметри моделей для досягнення кращих результатів.

- [Hyperparameter Tuning with Keras Tuner](https://www.tensorflow.org/tutorials/keras/keras_tuner)  
  Туторіал, який показує, як використовувати Keras Tuner для автоматичного підбору гіперпараметрів.

### 5. **Візуалізація та аналіз**
- [Visualizing Neural Networks with TensorBoard](https://www.tensorflow.org/tensorboard)  
  Інструмент для візуалізації процесу навчання нейронних мереж, включаючи графіки втрат та точності.

- [Confusion Matrix in Machine Learning](https://towardsdatascience.com/understanding-confusion-matrix-a9ad42dcfd62)  
  Стаття, яка пояснює, як інтерпретувати confusion matrix для оцінки якості класифікації.

### 6. **Додаткові матеріали**
- [Deep Learning with Python by François Chollet](https://www.manning.com/books/deep-learning-with-python)  
  Книга автора Keras, яка детально пояснює, як працювати з нейронними мережами за допомогою Keras.

- [Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow](https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/)  
  Практична книга, яка охоплює широкий спектр тем, включаючи роботу з Keras та TensorFlow.

- [Neural Networks and Deep Learning by Michael Nielsen](http://neuralnetworksanddeeplearning.com/)  
  Безкоштовна онлайн-книга, яка пояснює основи нейронних мереж та глибокого навчання.

### 7. **Інструменти для експериментів**
- [Google Colab](https://colab.research.google.com/)  
  Безкоштовний хмарний сервіс для роботи з Python та нейронними мережами. Підтримує GPU для прискорення навчання.

- [Weights & Biases](https://wandb.ai/)  
  Інструмент для відстеження експериментів, візуалізації результатів та порівняння моделей.

### 8. **Додаткові датасети для практики**
- [MNIST Dataset](http://yann.lecun.com/exdb/mnist/)  
  Класичний датасет для класифікації рукописних цифр. Може бути корисним для порівняння з Fashion MNIST.

- [CIFAR-10 Dataset](https://www.cs.toronto.edu/~kriz/cifar.html)  
  Датасет для класифікації кольорових зображень. Може бути корисним для більш складних завдань.

### 9. **Форуми та спільноти**
- [Stack Overflow](https://stackoverflow.com/questions/tagged/keras)  
  Питання та відповіді, пов’язані з Keras та нейронними мережами.

- [Reddit Machine Learning](https://www.reddit.com/r/MachineLearning/)  
  Спільнота, де можна обговорити питання, пов’язані з машинним навчанням.

- [Kaggle Kernels](https://www.kaggle.com/kernels)  
  Приклади роботи з різними датасетами, включаючи Fashion MNIST.

### 10. **Корисні бібліотеки**
- [Scikit-learn](https://scikit-learn.org/stable/)  
  Бібліотека для машинного навчання, яка може бути корисною для попередньої обробки даних та оцінки моделей.

- [NumPy](https://numpy.org/)  
  Бібліотека для роботи з числовими даними.

- [Matplotlib](https://matplotlib.org/)  
  Бібліотека для візуалізації даних.

- [Pandas](https://pandas.pydata.org/)  
  Бібліотека для роботи з табличними даними.