import pickle

import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)
vectorizer = pickle.load(open("backend/vectorizer.pkl","rb"))

def detect_fake_news(text):

    vec = vectorizer.transform([text])

    probabilities = model.predict_proba(vec)[0]

    prob_real = probabilities[1]

    confidence = round(prob_real * 100, 2)

    if confidence >= 80:
        verdict = "Real News"

    elif confidence >= 50:
        verdict = "Likely Real News"

    elif confidence >= 30:
        verdict = "Likely Fake News"

    else:
        verdict = "Fake News"

    return {
        "credibility_score": confidence,
        "verdict": verdict
    }
