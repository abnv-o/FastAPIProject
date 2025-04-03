from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

# Load the model
try:
    model = joblib.load("pcos_self_assess_model.pkl")
except Exception as e:
    print(f"❌ Model Loading Error: {e}")
    raise RuntimeError(f"Error loading model: {e}")

# Define expected features (same as Flask app)
FEATURES = [
    "Age (yrs)", "Weight (Kg)", "Height(Cm)", "BMI",
    "Cycle length(days)", "Cycle(R/I)",
    "Weight gain(Y/N)", "hair growth(Y/N)",
    "Skin darkening (Y/N)", "Pimples(Y/N)",
    "Fast food (Y/N)", "Reg.Exercise(Y/N)"
]

# Define input schema
class PCOSInput(BaseModel):
    Age: int
    Weight: float
    Height: float
    BMI: float
    Cycle_length: int
    Cycle_regularity: int
    Weight_gain: str  # "yes"/"no"
    Hair_growth: str  # "yes"/"no"
    Skin_darkening: str  # "yes"/"no"
    Pimples: str  # "yes"/"no"
    Fast_food: int  # e.g., 2
    Exercise: int  # e.g., 0

# Function to preprocess input data
def preprocess_input(data: PCOSInput):
    processed = {
        "Age (yrs)": data.Age,
        "Weight (Kg)": data.Weight,
        "Height(Cm)": data.Height,
        "BMI": data.BMI,
        "Cycle length(days)": data.Cycle_length,
        "Cycle(R/I)": data.Cycle_regularity,
        "Weight gain(Y/N)": 1 if data.Weight_gain.lower() == "yes" else 0,
        "hair growth(Y/N)": 1 if data.Hair_growth.lower() == "yes" else 0,
        "Skin darkening (Y/N)": 1 if data.Skin_darkening.lower() == "yes" else 0,
        "Pimples(Y/N)": 1 if data.Pimples.lower() == "yes" else 0,
        "Fast food (Y/N)": data.Fast_food,
        "Reg.Exercise(Y/N)": data.Exercise,
    }
    return pd.DataFrame([processed])

@app.post("/predict")
def predict(data: PCOSInput):
    try:
        df = preprocess_input(data)
        prediction = model.predict(df)[0]
        probability = model.predict_proba(df)[0][1]

        return {
            "prediction": "Risk of PCOS" if prediction == 1 else "No Risk of PCOS",
            "confidence": round(probability, 2)
        }
    except Exception as e:
        print(f"❌ Prediction Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

