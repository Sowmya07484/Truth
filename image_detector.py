import numpy as np
import cv2
from PIL import Image
import tensorflow as tf
import os

# -----------------------------
# CONFIG
# -----------------------------
IMG_SIZE = 224
MODEL_PATH = "deepfake_detector.h5"

# -----------------------------
# SAFE MODEL LOADING
# -----------------------------
model = None

if os.path.exists(MODEL_PATH):
    try:
        model = tf.keras.models.load_model(MODEL_PATH)
        print("✅ Deepfake model loaded successfully.")
    except Exception as e:
        print(f"⚠ Error loading model: {e}")
        model = None
else:
    print("⚠ deepfake_detector.h5 not found. Running in fallback mode.")

# -----------------------------
# MAIN FUNCTION
# -----------------------------
def detect_fake_image(uploaded_file):

    try:
        # If model is not available
        if model is None:
            return {
                "score": 0,
                "verdict": "⚠ Model not loaded (deepfake_detector.h5 missing)"
            }

        # Read image
        image = Image.open(uploaded_file).convert("RGB")
        img = np.array(image)

        # Resize
        img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))

        # Normalize
        img = img / 255.0

        # Expand dims
        img = np.expand_dims(img, axis=0)

        # Prediction
        prediction = model.predict(img, verbose=0)[0][0]

        fake_probability = float((1 - prediction) * 100)
        real_probability = float(prediction * 100)

        # -----------------------------
        # YOUR LABEL MAP:
        # fake = 0, real = 1
        # -----------------------------

        if prediction > 0.5:
            verdict = "✅ Image Appears Real"
            score = real_probability
        else:
            verdict = "⚠ Possible Deepfake Image"
            score = fake_probability

        return {
            "score": round(score, 2),
            "verdict": verdict
        }

    except Exception as e:
        return {
            "score": 0,
            "verdict": f"Error processing image: {str(e)}"
        }
