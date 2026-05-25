import pandas as pd
import joblib
from sklearn.metrics import classification_report
from preprocessing.encoder import encode_columns

crew = pd.read_csv("data/crew.csv")
model = joblib.load("models/crew_type_model.pkl")

crew["target"] = (crew["role"] == "Captain").astype(int)

X = crew[["role", "aircraft_type", "base_airport"]]
X, _ = encode_columns(X, X.columns)
y = crew["target"]

pred = model.predict(X)
print(classification_report(y, pred))