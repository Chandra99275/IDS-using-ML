import pandas as pd
from preprocess import load_data
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

X, y = load_data()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ✅ PASTE HERE
X_test = pd.DataFrame(X_test, columns=X_train.columns)

model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
