# import streamlit as st
# import gdown
# import os
# from keras.models import load_model
# from keras.preprocessing import image
# import numpy as np
# from PIL import Image
# import matplotlib.pyplot as plt

# # URL моделей
# MODELS = {
#     "CNN": {
#         "model_url": "https://drive.google.com/uc?id=12T85ZRjZuF88_29kGyrlS5HV-jzz4wKQ",
#         "model_file": "advanced_cnn_model.h5",
#     },
#     "VGG16": {
#         "model_url": "https://drive.google.com/uc?id=1wqDtrnxcpJj1oZhOUjpu37b3_m-qGHwu",
#         "model_file": "vgg16_finetuned.h5",
#     },
# }


# def download_file(url, output):
#     if url == "":
#         return  # Якщо немає URL, пропускаємо
#     if not os.path.exists(output):
#         with st.spinner(f"Downloading {output}..."):
#             gdown.download(url, output, quiet=False)
#     else:
#         st.info(f"{output} already downloaded.")


# def load_history(path):
#     if os.path.exists(path):
#         data = np.load(path)
#         return data["loss"], data["val_loss"], data["accuracy"], data["val_accuracy"]
#     else:
#         return None, None, None, None


# def plot_training_history(loss, val_loss, accuracy, val_accuracy):
#     fig, ax = plt.subplots(1, 2, figsize=(12, 4))

#     ax[0].plot(loss, label="Training loss")
#     ax[0].plot(val_loss, label="Validation loss")
#     ax[0].set_title("Loss")
#     ax[0].legend()

#     ax[1].plot(accuracy, label="Training accuracy")
#     ax[1].plot(val_accuracy, label="Validation accuracy")
#     ax[1].set_title("Accuracy")
#     ax[1].legend()

#     st.pyplot(fig)


# def preprocess_image(img, target_size=(224, 224)):
#     img = img.resize(target_size)
#     img_array = image.img_to_array(img) / 255.0
#     img_array = np.expand_dims(img_array, axis=0)
#     return img_array


# def main():
#     st.title("Image Classification with CNN and VGG16")

#     # Вибір моделі
#     model_choice = st.selectbox("Choose model:", list(MODELS.keys()))
#     model_info = MODELS[model_choice]

#     # Завантаження моделі
#     download_file(model_info["model_url"], model_info["model_file"])
#     model = load_model(model_info["model_file"])

#     # Спроба завантажити історію (може бути відсутня)
#     history_file = model_info.get("history_file", None)
#     loss, val_loss, accuracy, val_accuracy = None, None, None, None
#     if history_file:
#         loss, val_loss, accuracy, val_accuracy = load_history(history_file)

#     # Завантаження зображення для класифікації
#     uploaded_file = st.file_uploader(
#         "Upload an image for classification", type=["jpg", "jpeg", "png"]
#     )

#     if uploaded_file:
#         img = Image.open(uploaded_file).convert("RGB")
#         st.image(img, caption="Uploaded Image", use_column_width=True)

#         img_array = preprocess_image(img)

#         # Передбачення
#         predictions = model.predict(img_array)
#         predicted_class = np.argmax(predictions, axis=1)[0]

#         st.write(f"Predicted class index: {predicted_class}")
#         st.write("Class probabilities:")
#         st.write(predictions.flatten())

#     # Якщо історії немає, пропонуємо оцінити модель на валідних даних
#     st.markdown("---")
#     st.subheader("Evaluate model on validation dataset (optional)")

#     val_file = st.file_uploader(
#         "Upload validation data (.npz with 'x_val' and 'y_val')", type=["npz"]
#     )

#     if val_file:
#         val_data = np.load(val_file)
#         x_val = val_data["x_val"]
#         y_val = val_data["y_val"]

#         st.write(f"Validation data shape: {x_val.shape}, labels shape: {y_val.shape}")

#         # Оцінка моделі
#         loss_val, acc_val = model.evaluate(x_val, y_val, verbose=0)
#         st.write(f"Validation Loss: {loss_val:.4f}")
#         st.write(f"Validation Accuracy: {acc_val:.4f}")

#     # Якщо історія тренувань є, показуємо графіки
#     if loss is not None:
#         st.subheader("Training History")
#         plot_training_history(loss, val_loss, accuracy, val_accuracy)


# if __name__ == "__main__":
#     main()


# import streamlit as st
# import gdown
# import os
# import numpy as np
# from keras.models import load_model
# from keras.preprocessing import image
# import matplotlib.pyplot as plt
# from PIL import Image
# from keras.datasets import fashion_mnist

# # Class names for Fashion-MNIST
# CLASS_NAMES = [
#     "T-shirt/top",
#     "Trouser",
#     "Pullover",
#     "Dress",
#     "Coat",
#     "Sandal",
#     "Shirt",
#     "Sneaker",
#     "Bag",
#     "Ankle boot",
# ]

# # URL моделей
# MODELS = {
#     "CNN": {
#         "model_url": "https://drive.google.com/uc?id=12T85ZRjZuF88_29kGyrlS5HV-jzz4wKQ",
#         "model_file": "advanced_cnn_model.h5",
#     },
#     "VGG16": {
#         "model_url": "https://drive.google.com/uc?id=1wqDtrnxcpJj1oZhOUjpu37b3_m-qGHwu",
#         "model_file": "vgg16_finetuned.h5",
#     },
# }


# def download_file(url, output):
#     if url == "":
#         return
#     if not os.path.exists(output):
#         with st.spinner(f"Downloading {output}..."):
#             gdown.download(url, output, quiet=False)
#     else:
#         st.info(f"{output} already downloaded.")


# def plot_training_history(loss, val_loss, accuracy, val_accuracy):
#     fig, ax = plt.subplots(1, 2, figsize=(12, 4))

#     ax[0].plot(loss, label="Training loss")
#     ax[0].plot(val_loss, label="Validation loss")
#     ax[0].set_title("Loss")
#     ax[0].legend()

#     ax[1].plot(accuracy, label="Training accuracy")
#     ax[1].plot(val_accuracy, label="Validation accuracy")
#     ax[1].set_title("Accuracy")
#     ax[1].legend()

#     st.pyplot(fig)


# def plot_prediction_probabilities(predictions):
#     fig, ax = plt.subplots(figsize=(10, 5))
#     ax.bar(CLASS_NAMES, predictions)
#     ax.set_ylabel("Probability")
#     ax.set_xlabel("Class")
#     ax.set_title("Prediction Probabilities")
#     plt.xticks(rotation=45)
#     st.pyplot(fig)


# def preprocess_image_fmnist(img, model_choice):
#     if model_choice == "CNN":
#         # Fashion-MNIST: 28x28 grayscale
#         img = img.convert("L")  # grayscale
#         img = img.resize((28, 28))
#         img_array = image.img_to_array(img) / 255.0
#         img_array = np.expand_dims(img_array, axis=-1)  # add channel dim
#     else:
#         # VGG16: 224x224 RGB
#         img = img.convert("RGB")
#         img = img.resize((224, 224))
#         img_array = image.img_to_array(img) / 255.0
#     img_array = np.expand_dims(img_array, axis=0)
#     return img_array

# def main():
#     st.title("Fashion-MNIST Classification with CNN and VGG16")

#     # Model selection
#     model_choice = st.selectbox("Choose model:", list(MODELS.keys()))
#     model_info = MODELS[model_choice]

#     # Download & load model
#     download_file(model_info["model_url"], model_info["model_file"])
#     model = load_model(model_info["model_file"])

#     # Load Fashion-MNIST dataset
#     (_, _), (x_test, y_test) = fashion_mnist.load_data()

#     # Convert grayscale to RGB for display
#     x_test_rgb = np.stack([x_test] * 3, axis=-1)

#     # Select an image from dataset
#     idx = st.slider("Select test image index", 0, len(x_test) - 1, 0)
#     img = Image.fromarray(x_test_rgb[idx])

#     # Show the image
#     st.image(img, caption=f"True label: {CLASS_NAMES[y_test[idx]]}", width=200)

#     # Prepare for prediction
#     img_array = preprocess_image_fmnist(img, model_choice)

#     # Predict
#     predictions = model.predict(img_array)
#     predicted_class = np.argmax(predictions, axis=1)[0]
#     plot_prediction_probabilities(predictions)

#     st.write(f"Predicted class: **{CLASS_NAMES[predicted_class]}**")
#     st.write("Class probabilities:")
#     st.bar_chart(predictions.flatten())


# if __name__ == "__main__":
#     main()


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
    "VGG16": {
        "model_url": "https://drive.google.com/uc?id=1wqDtrnxcpJj1oZhOUjpu37b3_m-qGHwu",
        "model_file": "vgg16_finetuned.h5",
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
    else:
        # VGG16: 224x224 RGB
        img = img.convert("RGB")
        img = img.resize((224, 224))
        img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


def main():
    st.title("Fashion-MNIST Classification with CNN and VGG16")

    # Вибір моделі
    model_choice = st.selectbox("Choose model:", list(MODELS.keys()))
    model_info = MODELS[model_choice]

    # Завантаження і підвантаження моделі
    download_file(model_info["model_url"], model_info["model_file"])
    model = (
        load_model(model_info["model_file"])
        if model_choice == "CNN"
        else load_model(
            model_info["model_file"],
            compile=False,
            custom_objects={"Functional": tf.keras.models.Model},
        )
    )

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
