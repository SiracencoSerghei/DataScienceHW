import streamlit as st
import gdown
import os
import numpy as np
import tensorflow as tf
from keras.models import load_model
from keras.preprocessing import image
import matplotlib.pyplot as plt
from PIL import Image
from keras.datasets import fashion_mnist

# Класи Fashion-MNIST
CLASS_NAMES = [
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle boot",
]

# URL моделей
MODELS = {
    "CNN": {
        "model_url": "https://drive.google.com/uc?id=12T85ZRjZuF88_29kGyrlS5HV-jzz4wKQ",
        "model_file": "advanced_cnn_model.h5",
    },
    # "VGG16": {
    #     "model_url": "https://drive.google.com/uc?id=1vLp_sn50BeMAwPIJtlNOrzi0m-9Yw2UB",
    #     "model_file": "vgg16_finetuned.h5",
    #     # https://drive.google.com/file/d/1vLp_sn50BeMAwPIJtlNOrzi0m-9Yw2UB/view?usp=drive_link
    # },
    "VGG16": {
        "model_url": "https://drive.google.com/uc?id=1oaJegoBrBTm7XE8zjOW4CvqwlOwtEhpi",
        "model_file": "vgg16_finetuned_stage2.h5",
        # https://drive.google.com/file/d/1oaJegoBrBTm7XE8zjOW4CvqwlOwtEhpi/view?usp=drive_link
    },
}


def download_file(url, output):
    if url == "":
        return
    if not os.path.exists(output):
        with st.spinner(f"Downloading {output}..."):
            gdown.download(url, output, quiet=False)
    else:
        st.info(f"{output} already downloaded.")


def plot_prediction_probabilities(predictions):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(CLASS_NAMES, predictions.flatten())
    ax.set_ylabel("Probability")
    ax.set_xlabel("Class")
    ax.set_title("Prediction Probabilities")
    plt.xticks(rotation=45)
    st.pyplot(fig)


def preprocess_image_fmnist(img, model_choice):
    if model_choice == "CNN":
        # Fashion-MNIST: 28x28 grayscale
        img = img.convert("L")  # в градаціях сірого
        img = img.resize((28, 28))
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=-1)  # додати канал
    else:  # VGG16
        img = img.convert("RGB")
        img = img.resize((48, 48))  # Замість 224х224 робимо 48х48
        img_array = image.img_to_array(img) / 255.0

    img_array = np.expand_dims(img_array, axis=0)
    return tf.convert_to_tensor(img_array)


def main():
    st.title("Fashion-MNIST Classification with CNN and VGG16")

    # Вибір моделі
    model_choice = st.selectbox("Choose model:", list(MODELS.keys()))
    model_info = MODELS[model_choice]

    # Завантажуємо модель локально (якщо ще нема)
    download_file(model_info["model_url"], model_info["model_file"])

    # Завантажуємо модель з локального файлу (НЕ з URL!)
    model = load_model(model_info["model_file"])

    # Завантажуємо тестовий набір Fashion-MNIST
    (_, _), (x_test, y_test) = fashion_mnist.load_data()

    # Конвертуємо в RGB для відображення
    x_test_rgb = np.stack([x_test] * 3, axis=-1)

    # Обираємо індекс зображення для тесту
    idx = st.slider("Select test image index", 0, len(x_test) - 1, 0)
    img = Image.fromarray(x_test_rgb[idx])

    # Показуємо зображення
    st.image(img, caption=f"True label: {CLASS_NAMES[y_test[idx]]}", width=200)

    # Підготовка зображення для передбачення
    img_array = preprocess_image_fmnist(img, model_choice)

    # Передбачення
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions, axis=1)[0]

    st.write(f"Predicted class: **{CLASS_NAMES[predicted_class]}**")
    st.write("Class probabilities:")
    st.bar_chart(predictions.flatten())

    # Виводимо ймовірності у вигляді графіка
    plot_prediction_probabilities(predictions)


if __name__ == "__main__":
    main()
