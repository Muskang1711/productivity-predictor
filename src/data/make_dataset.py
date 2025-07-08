import pandas as pd
import numpy as np
import os

np.random.seed(42)

def generate_data(n_samples = 500):
    data = pd.DataFrame({
        "sleep_hours": np.random.normal(7,1.5,n_samples).clip(4,10),
        "screen_time":np.random.normal(6,2,n_samples).clip(2,12),
        "breaks_taken":np.random.randint(1,10,n_samples),
        "exercise_minutes": np.random.normal(50,15, n_samples).clip(0, 90),
        "hydration_liters": np.random.normal(2, 0.5, n_samples).clip(1, 4),
        "work_hours": np.random.normal(8, 1.5, n_samples).clip(4, 12)
    })


    data["productivity_score"] = (
        data["sleep_hours"] *5
        +data["exercise_minutes"] * 0.3
        + data["hydration_liters"] * 3
        + data["work_hours"] * 4
        - data["screen_time"] * 2
        - data["breaks_taken"] * 1.5
        + np.random.normal(0, 10, n_samples)
    ).clip(0, 100).round(2)


   # Classification label
    def score_to_label(score):
        if score < 40:
            return "Low"
        elif score < 70:
            return "Medium"
        else:
            return "High"
    
    data["productivity_label"] = data["productivity_score"].apply(score_to_label)

    return data

def save_data():
    data = generate_data()
    output_path = "data/raw/productivity_data.csv"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    data.to_csv(output_path, index=False)
    print(f"✅ Data saved to: {output_path}")

if __name__ == "__main__":
    save_data()