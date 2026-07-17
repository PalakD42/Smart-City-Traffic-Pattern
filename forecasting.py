import os
import pandas as pd
import matplotlib.pyplot as plt

from statsmodels.tsa.arima.model import ARIMA

os.makedirs("output/forecast", exist_ok=True)


def forecast(df):

    print("\n" + "="*50)
    print("ARIMA FORECASTING")
    print("="*50)

    # Average traffic of all junctions
    traffic = df.groupby("DateTime")["Vehicles"].mean()
    
    traffic = traffic.asfreq("h")

    traffic = traffic.ffill()

    # Build ARIMA Model
    model = ARIMA(traffic, order=(5,1,0))

    model_fit = model.fit()

    print("ARIMA Model Trained Successfully!")

    # Forecast next 96 hours (4 days)
    future = model_fit.forecast(steps=96)

    # Save Forecast
    forecast_df = pd.DataFrame({
        "Forecasted Traffic": future
    })

    forecast_df.to_csv(
        "output/forecast/future_forecast.csv",
        index=False
    )

    # Plot Forecast
    plt.figure(figsize=(15,6))

    plt.plot(
        traffic[-300:],
        label="Historical Traffic"
    )

    plt.plot(
        future,
        label="Forecast",
        color="red"
    )

    plt.title("Future Traffic Forecast")

    plt.xlabel("Time")

    plt.ylabel("Vehicles")

    plt.legend()

    plt.grid(True)

    plt.savefig(
        "output/forecast/future_forecast.png"
    )

    plt.close()

    print("Forecast Saved Successfully!")