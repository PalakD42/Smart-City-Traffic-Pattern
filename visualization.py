import os
import matplotlib.pyplot as plt


os.makedirs("output/graphs", exist_ok=True)

def create_graphs(df):

    print("\nCreating Graphs...")

    plt.figure(figsize=(15,6))
    plt.plot(df["DateTime"], df["Vehicles"])
    plt.title("Traffic Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Vehicles")
    plt.grid(True)
    plt.savefig("output/graphs/traffic_trend.png")
    plt.close()


    plt.figure(figsize=(8,5))
    junction = df.groupby("Junction")["Vehicles"].mean()
    plt.bar(junction.index.astype(str), junction.values)
    plt.title("Average Traffic by Junction")
    plt.xlabel("Junction")
    plt.ylabel("Average Vehicles")
    plt.savefig("output/graphs/junction_average.png")
    plt.close()


    plt.figure(figsize=(12,5))
    hourly = df.groupby("Hour")["Vehicles"].mean()
    plt.plot(hourly.index, hourly.values, marker="o")
    plt.title("Average Hourly Traffic")
    plt.xlabel("Hour")
    plt.ylabel("Vehicles")
    plt.grid(True)
    plt.savefig("output/graphs/hourly_traffic.png")
    plt.close()

   
    plt.figure(figsize=(8,5))
    monthly = df.groupby("Month")["Vehicles"].mean()
    plt.plot(monthly.index, monthly.values, marker="o")
    plt.title("Average Monthly Traffic")
    plt.xlabel("Month")
    plt.ylabel("Vehicles")
    plt.grid(True)
    plt.savefig("output/graphs/monthly_traffic.png")
    plt.close()

  
    plt.figure(figsize=(10,5))
    weekday = df.groupby("Weekday")["Vehicles"].mean()
    plt.bar(weekday.index, weekday.values)
    plt.xticks(rotation=45)
    plt.title("Average Weekday Traffic")
    plt.savefig("output/graphs/weekday_traffic.png")
    plt.close()

  
   
    plt.figure(figsize=(8,5))
    plt.hist(df["Vehicles"], bins=30)
    plt.title("Vehicle Distribution")
    plt.savefig("output/graphs/vehicle_distribution.png")
    plt.close()

    
    plt.figure(figsize=(15,6))

    for j in sorted(df["Junction"].unique()):
        temp = df[df["Junction"] == j]
        plt.plot(temp["DateTime"], temp["Vehicles"], label=f"Junction {j}")

    plt.legend()
    plt.title("Traffic at All Junctions")
    plt.grid(True)
    plt.savefig("output/graphs/all_junctions.png")
    plt.close()

    print("All graphs saved successfully!")