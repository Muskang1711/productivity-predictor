import pandas as pd 
import numpy as np
import os
import mlflow
import mlflow.sklearn
import mlflow.xgboost
from box import ConfigBox
import yaml

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, f1_score

from sklearn.model_selection import train_test_split

def convert_To_class(score):
    if score< 40:
        return "low"
    elif score < 70:
        return "medium"
    else:
        return "high"
    

def train_and_log_model(model,model_name, X_train,X_test,y_train, y_test,y_test_class):
    with mlflow.start_run(run_name = model_name):
        model.fit(X_train,y_train)

        preds =model.predict(X_test)

        mse = mean_squared_error(y_test,preds)
        r2 = r2_score(y_test,preds)

        pred_class = [convert_To_class(p) for p in preds]

        f1 = f1_score(y_test_class,pred_class,average = 'weighted')


        mlflow.log_param("model_type", model_name)
        mlflow.log_metric("mse",mse)
        mlflow.log_metric("r2_score",r2)
        mlflow.log_metric("f1_score",f1)

        if model_name == "XGBoost":
            mlflow.xgboost.log_model(model,f"{model_name}_model")
        else:
            mlflow.sklearn.log_model(model, f"{model_name}_model")

        print(f"{model_name} logged to MLflow")

def main():
    
    params = ConfigBox(yaml.safe_load(open("params.yaml")))["train"]
    df = pd.read_csv("data/raw/productivity_data.csv")

    X = df.drop(columns = [params.target,"productivity_label"])

    y= df[params.target]
    y_class = df["productivity_label"]


    X_train, X_test, y_train, y_test, y_class_train, y_class_test = train_test_split(
        X, y, y_class, test_size=params.test_size, random_state=params.random_state
    )

  models = {}

    if "LinearRegression" in params.model_list:
        models["LinearRegression"] = LinearRegression()

    if "RandomForest" in params.model_list:
        models["RandomForest"] = RandomForestRegressor(n_estimators=params.n_estimators)

    if "XGBoost" in params.model_list:
        models["XGBoost"] = XGBRegressor(n_estimators=params.n_estimators, verbosity=0)

    # 🔁 Train and log all models
    for name, model in models.items():
        train_and_log_model(model, name, X_train, X_test, y_train, y_test, y_class_test)

if __name__ == "__main__":
    main()
    


    
