from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import os

# 🔹 Input Schema: Based on the features from your data generation
class ProductivityInput(BaseModel):
    sleep_hours: float
    screen_time: float
    breaks_taken: int
    exercise_minutes: float
    hydration_liters: float
    work_hours: float

# 🔹 Load model from models/RandomForest_model/model.pkl
model_path = os.path.join("models", "RandomForest_model", "model.pkl")

if not os.path.exists(model_path):
    raise FileNotFoundError(f"❌ Model file not found at {model_path}")

model = joblib.load(model_path)

# 🔹 Initialize FastAPI app
app = FastAPI(title="🧠 Productivity Predictor API")

@app.get("/")
def read_root():
    return {"message": "🚀 Welcome to the Productivity Predictor API!"}

@app.post("/predict")
def predict(data: ProductivityInput):
    # Convert input to DataFrame
    input_df = pd.DataFrame([data.dict()])

    # Predict using the model
    prediction = model.predict(input_df)[0]

    # Convert prediction to label
    if prediction < 40:
        label = "Low"
    elif prediction < 70:
        label = "Medium"
    else:
        label = "High"

    return {
        "predicted_productivity_score": float(prediction),
        "productivity_label": label
    }
