import pandas as pd
import os

def load_data():

    print("=" * 60)
    print("SMART CITY TRAFFIC DATASET")
    print("=" * 60)

    # Load Dataset
    file_path = os.path.join("data", "train_aWnotuB.csv")
    df = pd.read_csv(file_path)

    print("\nFirst 5 Rows")
    print(df.head())

    print("\nDataset Shape")
    print(df.shape)

    print("\nColumn Names")
    print(df.columns.tolist())

    print("\nDataset Information")
    print(df.info())

    print("\nMissing Values")
    print(df.isnull().sum())

    # Convert DateTime column
    df["DateTime"] = pd.to_datetime(df["DateTime"])

    # Create New Features
    df["Year"] = df["DateTime"].dt.year
    df["Month"] = df["DateTime"].dt.month
    df["Day"] = df["DateTime"].dt.day
    df["Hour"] = df["DateTime"].dt.hour
    df["Minute"] = df["DateTime"].dt.minute
    df["Weekday"] = df["DateTime"].dt.day_name()

    # Convert Weekday to Numerical Values
    weekday_map = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6
    }

    df["Weekday"] = df["Weekday"].map(weekday_map)

    # Sort by DateTime
    df = df.sort_values("DateTime")

    # Reset Index
    df.reset_index(drop=True, inplace=True)

    # Remove Duplicate Rows
    df.drop_duplicates(inplace=True)

    print("\nUpdated Dataset")
    print(df.head())

    print("\nData Types")
    print(df.dtypes)

    print("\nStatistical Summary")
    print(df.describe())

    print("\nPreprocessing Completed Successfully!")

    return df
