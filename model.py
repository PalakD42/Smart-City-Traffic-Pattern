import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


os.makedirs("output/predictions", exist_ok=True)


def train_model(df):

    print("\n" + "=" * 50)
    print("RANDOM FOREST MODEL")
    print("=" * 50)

    # Features
    X = df[[
        "Junction",
        "Hour",
        "Day",
        "Month",
        "Year"
    ]]

    # Target
    y = df["Vehicles"]

    # Train-Test Split (80:20)
    split = int(len(df) * 0.8)

    X_train = X.iloc[:split]
    X_test = X.iloc[split:]

    y_train = y.iloc[:split]
    y_test = y.iloc[split:]

    print(f"Training Samples : {len(X_train)}")
    print(f"Testing Samples  : {len(X_test)}")

    # Train Model
    model = RandomForestRegressor(
        n_estimators=100,
        max_depth=15,
        random_state=42,
        n_jobs=-1
    )

    print("\nTraining Model...")
    model.fit(X_train, y_train)

    print("Model Trained Successfully!")

    # Prediction
    prediction = model.predict(X_test)

    # Evaluation
    mae = mean_absolute_error(y_test, prediction)
    rmse = np.sqrt(mean_squared_error(y_test, prediction))
    r2 = r2_score(y_test, prediction)

    print("\nModel Performance")
    print("--------------------------")
    print(f"MAE      : {mae:.2f}")
    print(f"RMSE     : {rmse:.2f}")
    print(f"R² Score : {r2:.4f}")

    # Save Prediction CSV
    result = pd.DataFrame({
        "Actual": y_test.values,
        "Predicted": prediction
    })

    result.to_csv(
        "output/predictions/model_results.csv",
        index=False
    )

    # Graph
    plt.figure(figsize=(14,6))

    plt.plot(
        y_test.values[:300],
        label="Actual",
        linewidth=2
    )

    plt.plot(
        prediction[:300],
        label="Predicted",
        linewidth=2
    )

    plt.title("Actual vs Predicted Traffic")

    plt.xlabel("Samples")

    plt.ylabel("Vehicles")

    plt.legend()

    plt.grid(True)

    plt.savefig(
        "output/predictions/actual_vs_predicted.png"
    )

    plt.close()

    print("\nPrediction graph saved.")

    return model