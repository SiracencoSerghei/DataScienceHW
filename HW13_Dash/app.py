import os
import numpy as np
import gdown
import tensorflow as tf
from keras.models import load_model
from keras.preprocessing import image
from keras.datasets import fashion_mnist
from PIL import Image
import io
import base64
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go

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
        "model_url": "https://drive.google.com/uc?id=1vLp_sn50BeMAwPIJtlNOrzi0m-9Yw2UB",
        "model_file": "vgg16_finetuned.h5",
        # https://drive.google.com/file/d/1vLp_sn50BeMAwPIJtlNOrzi0m-9Yw2UB/view?usp=drive_link
    },
    # "VGG16": {
    #     "model_url": "https://drive.google.com/uc?id=1oaJegoBrBTm7XE8zjOW4CvqwlOwtEhpi",
    #     "model_file": "vgg16_finetuned_stage2.h5",
    # },
}


# Функція для завантаження файлу
def download_file(url, output):
    if not os.path.exists(output):
        gdown.download(url, output, quiet=False)


# Передобробка зображення
def preprocess_image_fmnist(img, model_choice):
    if model_choice == "CNN":
        img = img.convert("L")
        img = img.resize((28, 28))
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=-1)
    else:  # VGG16
        img = img.convert("RGB")
        img = img.resize((48, 48))
        img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return tf.convert_to_tensor(img_array)


# Завантажуємо тестові дані
(_, _), (x_test, y_test) = fashion_mnist.load_data()
x_test_rgb = np.stack([x_test] * 3, axis=-1)

# Ініціалізація Dash
app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.H1("Fashion-MNIST Classification with CNN and VGG16"),
        html.Div([
            html.Label("Choose model:"),
            dcc.Dropdown(
                id="model_choice",
                options=[{"label": k, "value": k} for k in MODELS.keys()],
                value="CNN",
                style={"width": "90%"} 
                    ),
                ],
                style={
                    "width": "40%", 
                    "minWidth": "250px",
                    "margin": "10px auto"
                }),
        html.Label("Select test image index:"),
        dcc.Slider(id="img_index", min=0, max=len(x_test) - 1, step=1, value=0),
        html.Img(id="test_image", style={"width": "200px", "margin-top": "10px"}),
        html.Button(
            "Predict", id="predict_btn", n_clicks=0, style={"margin-top": "20px"}
        ),
        html.Div(id="true_label", style={"margin-top": "10px", "font-weight": "bold", "text-align": "center"}),
        html.Div(
            id="predicted_class", style={"margin-top": "10px", "font-weight": "bold"}
        ),
        dcc.Graph(id="probabilities_graph"),
    ]
)


@app.callback(
    [Output("test_image", "src"), Output("true_label", "children")],
    Input("img_index", "value"),
)
def update_image(idx):
    img = Image.fromarray(x_test_rgb[idx])
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    encoded = base64.b64encode(buffer.getvalue()).decode()
    return f"data:image/png;base64,{encoded}", f"True label: {CLASS_NAMES[y_test[idx]]}"


@app.callback(
    [Output("predicted_class", "children"), Output("probabilities_graph", "figure")],
    [Input("predict_btn", "n_clicks")],
    [State("model_choice", "value"), State("img_index", "value")],
)
def predict(n_clicks, model_choice, idx):
    if n_clicks == 0:
        return "", go.Figure()

    model_info = MODELS[model_choice]
    download_file(model_info["model_url"], model_info["model_file"])
    model = load_model(model_info["model_file"])

    img = Image.fromarray(x_test_rgb[idx])
    img_array = preprocess_image_fmnist(img, model_choice)

    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions, axis=1)[0]

    fig = go.Figure(data=[go.Bar(x=CLASS_NAMES, y=predictions.flatten())])
    fig.update_layout(
        title="Prediction Probabilities", xaxis_title="Class", yaxis_title="Probability"
    )

    return f"Predicted class: {CLASS_NAMES[predicted_class]}", fig


if __name__ == "__main__":
    app.run(debug=True)
