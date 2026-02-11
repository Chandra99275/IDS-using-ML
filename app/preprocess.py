import os
import joblib
from scapy.all import sniff, IP

# Absolute path fix (THIS SOLVES YOUR ERROR)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'model', 'ids_model.pkl')

# Load trained model
model = joblib.load(MODEL_PATH)

alerts = []

def extract_features(packet):
    if IP in packet:
        return [
            0,1,1,1,len(packet),0,
            0,0,0,0,0,1,0,0,0,0,0,0,0,0,
            0,0,10,10,0,0,0,0,1,0,0,255,
            255,0,0,0,0,0,0,0,0
        ]
    return None

def process_packet(packet):
    features = extract_features(packet)
    if features:
        result = model.predict([features])[0]
        if result == 1:
            alerts.append("⚠️ Intrusion Detected")

def start_ids():
    sniff(prn=process_packet, store=0)
