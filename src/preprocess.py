import pandas as pd
import numpy as np

def load_data():
    print("Loading CIC-IDS-2017 dataset...")

    df = pd.read_csv("../dataset/cic_ids.csv")

    print("Dataset shape:", df.shape)

    # Clean column names
    df.columns = df.columns.str.strip()

    # Drop non-ML columns
    df = df.drop(columns=["Flow ID", "Timestamp"], errors="ignore")

    # Convert label
    df["Label"] = df["Label"].apply(
        lambda x: 0 if x == "BENIGN" else 1
    )

    # Replace infinite values with NaN
    df.replace([np.inf, -np.inf], np.nan, inplace=True)

    # Drop rows with NaN
    df.dropna(inplace=True)

    print("Cleaned dataset shape:", df.shape)

    X = df.drop("Label", axis=1)
    y = df["Label"]

    return X, y
