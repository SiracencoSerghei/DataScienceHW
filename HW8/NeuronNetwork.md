Алгоритм прямого розповсюдження сигналу (forward propagation) та зворотного розповсюдження помилки (backpropagation) є основними компонентами нейронних мереж для навчання моделей. Ось короткий опис кожного з них:

## 1. Пряме розповсюдження сигналу (Forward Propagation)
Пряме розповсюдження сигналу — це процес, коли вхідні дані проходять через нейронну мережу до її виходу. Це основний етап, коли дані подаються на вхід і обчислюються виводи кожного шару мережі.

### Кроки:
- Вхідні дані передаються на перший шар.
- Для кожного шару мережі:
  1. Обчислюється лінійна комбінація входів: 
     $$ z = w \cdot x + b $$ 
     де \( w \) — ваги, \( x \) — вхід, \( b \) — зміщення (bias).
  2. Застосовується активаційна функція 
     $$ a = f(z) $$ 
     де \( f \) може бути, наприклад, сигмоїдною, ReLU, тощо.
- Результат, отриманий на останньому шарі, є передбаченням мережі.

## 2. Зворотне розповсюдження помилки (Backpropagation)
Зворотне розповсюдження помилки — це алгоритм для навчання нейронної мережі, який дозволяє оптимізувати ваги мережі за допомогою градієнтного спуску.

### Кроки:
- Після того, як отримано передбачення мережі, обчислюється помилка (втрата) між передбаченням і реальними значеннями за допомогою функції втрат (наприклад, середньоквадратичної помилки або крос-ентропії).
- Потім градієнт помилки розповсюджується через мережу, починаючи з останнього шару і рухаючись до першого.
  1. Обчислюються часткові похідні функції втрат щодо ваг кожного шару.
  2. Ваги оновлюються за допомогою градієнтного спуску: 
     $$ w = w - \eta \cdot \frac{\partial L}{\partial w} $$ 
де $\eta$ — швидкість навчання (learning rate), \( L \) — функція втрат.

- Цей процес повторюється до досягнення мінімальної помилки.

## Де знайти інформацію:

### Книги:
- **[Deep Learning](https://www.deeplearningbook.org/)** Іен Гудфеллоу, Йошуа Бенджіо, Аарона Курвіля. Це одна з найкращих книг, щоб глибше зрозуміти теорію нейронних мереж, включаючи forward propagation та backpropagation.
- **[Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/)** Майкл Нільсен. Це онлайн-книга, яка охоплює основи нейронних мереж та алгоритмів зворотного розповсюдження.

### Онлайн-курси:
- **[Coursera — Deep Learning Specialization](https://www.coursera.org/specializations/deep-learning)** від Andrew Ng. Включає теорію та практичні завдання, пов'язані з алгоритмами навчання нейронних мереж.
- **[Fast.ai](https://www.fast.ai/)** — курс, що містить навчальні матеріали щодо побудови нейронних мереж та глибокого навчання.

### Статті та блоги:
- **[Medium](https://medium.com/)** — на платформі багато статей про машинне навчання, в тому числі з описами forward propagation та backpropagation.
- **[Towards Data Science](https://towardsdatascience.com/)** — ще один корисний ресурс для розуміння нейронних мереж.

### Документація бібліотек:
- **[TensorFlow](https://www.tensorflow.org/)** та **[PyTorch](https://pytorch.org/)** мають відмінні документи, де можна знайти реалізації та теоретичні роз'яснення цих алгоритмів.
