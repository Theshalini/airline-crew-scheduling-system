import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from preprocessing.encoder import encode_columns

crew = pd.read_csv("data/crew.csv")

crew["target"] = (crew["role"] == "Captain").astype(int)

X = crew[["role", "aircraft_type", "base_airport"]]
X, _ = encode_columns(X, X.columns)
y = crew["target"]

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

joblib.dump(model, "models/crew_type_model.pkl")
print("✅ Crew type model trained & saved")