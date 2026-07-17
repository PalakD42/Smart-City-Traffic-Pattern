from preprocessing import load_data
from visualization import create_graphs
from model import train_model
from forecasting import forecast


def main():

    print("=" * 60)
    print("      SMART CITY TRAFFIC PATTERN FORECASTING")
    print("=" * 60)

    # Step 1: Load and Preprocess Data
    print("\nStep 1: Loading and Preprocessing Data...")
    df = load_data()

    # Step 2: Data Visualization
    print("\nStep 2: Creating Visualizations...")
    create_graphs(df)

    # Step 3: Train Machine Learning Model
    print("\nStep 3: Training Random Forest Model...")
    model = train_model(df)

    # Step 4: Forecast Future Traffic
    print("\nStep 4: Forecasting Future Traffic...")
    forecast(df)

    print("\n" + "=" * 60)
    print("PROJECT COMPLETED SUCCESSFULLY!")
    print("=" * 60)


# Run Project
if __name__ == "__main__":
    main()