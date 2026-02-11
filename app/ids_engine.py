import threading
import time
import joblib
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model = joblib.load(os.path.join(BASE_DIR, "model", "ids_model.pkl"))
feature_names = joblib.load(os.path.join(BASE_DIR, "model", "features.pkl"))

alerts = []   # shared alerts list


def extract_dummy_features():
    """
    Dummy real-time feature generator
    (used for live demo instead of real packet parsing)
    """
    return [0] * len(feature_names)


def start_ids():
    """
    Starts IDS monitoring in background thread
    """
    def run():
        while True:
            features = extract_dummy_features()
            df = pd.DataFrame([features], columns=feature_names)
            prediction = model.predict(df)[0]

            if prediction != "normal":
                alerts.append("⚠️ Intrusion Detected")

            time.sleep(2)

    thread = threading.Thread(target=run, daemon=True)
    thread.start()
