import pandas as pd
import numpy as np
import os
import mlflow
import mlflow.sklearn
import mlflow.xgboost
from box import ConfigBox
import yaml
import joblib

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score, f1_score
from sklearn.model_selection import train_test_split


# 🎯 Convert score to label
def convert_to_class(score):
    if score < 40:
        return "low"
    elif score < 70:
        return "medium"
    else:
        return "high"


# 🔁 Train + Evaluate + Log to MLflow
def train_and_log_model(model, model_name, X_train, X_test, y_train, y_test, y_test_class):
    with mlflow.start_run(run_name=model_name):
        model.fit(X_train, y_train)
        preds = model.predict(X_test)

        mse = mean_squared_error(y_test, preds)
        r2 = r2_score(y_test, preds)

        pred_class = [convert_to_class(p) for p in preds]
        f1 = f1_score(y_test_class, pred_class, average='weighted')

        mlflow.log_param("model_type", model_name)
        mlflow.log_metric("mse", mse)
        mlflow.log_metric("r2_score", r2)
        mlflow.log_metric("f1_score", f1)

         # 🔽 Save model manually into models/ for DVC to track
        os.makedirs("models", exist_ok=True)
        if model_name == "XGBoost":
            mlflow.xgboost.save_model(model, f"models/{model_name}_model")
        else:
            mlflow.sklearn.save_model(model, f"models/{model_name}_model")
        
        joblib.dump(model, "models/model.pkl")
        print(f"✅ {model_name} logged and saved to models/")


def main():
    # 📖 Load parameters
    params = ConfigBox(yaml.safe_load(open("params.yaml")))["train"]
    csv_path = os.path.join("data", "raw", "productivity_data.csv")
    df = pd.read_csv(csv_path)


    X = df.drop(columns=[params.target, "productivity_label"])
    y = df[params.target]
    y_class = df["productivity_label"]

    # ✂️ Split
    X_train, X_test, y_train, y_test, y_class_train, y_class_test = train_test_split(
        X, y, y_class, test_size=params.test_Size, random_state=params.random_state
    )

    models = {}

    if "LinearRegression" in params.model_list:
        models["LinearRegression"] = LinearRegression()

    if "RandomForest" in params.model_list:
        models["RandomForest"] = RandomForestRegressor(n_estimators=params.n_Estimators)

    if "XGBoost" in params.model_list:
        models["XGBoost"] = XGBRegressor(n_estimators=params.n_Estimators, verbosity=0)

    for name, model in models.items():
        train_and_log_model(model, name, X_train, X_test, y_train, y_test, y_class_test)


if __name__ == "__main__":
    main()



