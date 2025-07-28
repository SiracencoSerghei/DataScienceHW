# 📚 NLP Summary Task: README.md

## 🧠 Завдання

Сформуйте коротке текстове резюме англомовного тексту за допомогою **бібліотек NLTK та SpaCy**.

📌 **Вхідні дані:** історичний опис космічного човника *Discovery*.  
📌 **Результат:** текстове резюме, яке охоплює основну суть вихідного тексту.

---

## 🔧 Інструменти

### 1. 🐍 [NLTK (Natural Language Toolkit)](https://www.nltk.org/)

- **Можливості**:
  - Токенізація речень і слів
  - Стоп-слова
  - Частотний аналіз слів
  - Стемінг / лематизація (обмежено)
  - Побудова простого extractive summary
  
- **Основні імпорти**:
```python
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('punkt')
nltk.download('stopwords')
text = """..."""
sentences = sent_tokenize(text)
words = word_tokenize(text)
filtered = [w for w in words if w.lower() not in stopwords.words('english')]
```

### 2. ⚙️ SpaCy
- **Можливості:**
    - Потужна лематизація

    - Токенізація та POS-теги

    - Синтаксичний аналіз

    - Пошук іменованих сутностей

    - Формування якісних embeddings

- **Основні імпорти**:
```python
import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)
tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
```

### 🔁 Алгоритм extractive summarization (спільно з heapq)

```python
from heapq import nlargest

# Частотний словник слів
word_frequencies = {}
for word in doc:
    if word.text.lower() not in stopwords.words('english') and word.text.isalpha():
        word_frequencies[word.text.lower()] = word_frequencies.get(word.text.lower(), 0) + 1

# Нормалізація
max_freq = max(word_frequencies.values())
for word in word_frequencies:
    word_frequencies[word] /= max_freq

# Оцінювання речень
sentence_scores = {}
for sent in doc.sents:
    for word in sent:
        if word.text.lower() in word_frequencies:
            sentence_scores[sent] = sentence_scores.get(sent, 0) + word_frequencies[word.text.lower()]

# Резюме: top N речень
summary_sentences = nlargest(3, sentence_scores, key=sentence_scores.get)
summary = " ".join([sent.text for sent in summary_sentences])
print(summary)
```

### 📚 Додаткові матеріали

- 🔗 **NLTK**:
    [Офіційна документація](https://www.nltk.org/)

     [NLTK Book](https://www.nltk.org/book/)

      Стоп-слова, стемінг: nltk.corpus.stopwords, PorterStemmer

- 🔗 **SpaCy**:
  [Офіційна документація](https://spacy.io/usage)

    [Онлайн демо-парсер](https://demos.explosion.ai/displacy)

Моделі: en_core_web_sm, en_core_web_md, xx_ent_wiki_sm

- 📖 **Інше цікаве**:
📘 [Sumy](https://github.com/miso-belica/sumy) — ще одна бібліотека для extractive summarization

📘 [Gensim TextRank](https://radimrehurek.com/gensim/)

🧠 [BERTSum, Pegasus (Google)] — SOTA у abstractive summarization (потребують GPU)