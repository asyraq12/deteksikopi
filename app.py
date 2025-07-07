from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os
import json

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Load model dan label map
model = load_model("model.h5")
with open("label_map.json") as f:
    label_map = json.load(f)
label_map_rev = {v: k for k, v in label_map.items()}

# Pastikan input size betul
input_size = model.input_shape[1:3]

@app.route("/", methods=["GET", "POST"])
def index():
    label = None
    filename = None
    confidence = None

    if request.method == "POST":
        file = request.files.get("image")
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            # Preprocessing
            img = load_img(filepath, target_size=input_size)
            img_array = img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0) / 255.0

            # Prediction
            prediction = model.predict(img_array)[0]
            predicted_class = np.argmax(prediction)

            # Periksa apakah softmax ada di model:
            predicted_prob = np.max(prediction)
            confidence = round(float(predicted_prob) * 100, 2)

            label = label_map_rev.get(predicted_class, "Unknown")
            if confidence < 77 : 
                label = "Bukan Biji Kopi"
            filename = file.filename

    return render_template("index.html", label=label, filename=filename, confidence=confidence)

if __name__ == "__main__":
    app.run(debug=True)
