# 🚦 Smart City Traffic Pattern Prediction

A Machine Learning project that analyzes historical traffic data, visualizes traffic patterns, and predicts future traffic flow to support smart city traffic management.

---

## 📖 Overview

This project uses historical traffic data to analyze vehicle movement at different junctions and forecast future traffic patterns. It includes data preprocessing, visualization, machine learning model training, prediction, and forecasting.

---

## ✨ Features

- 📊 Data preprocessing and cleaning
- 📈 Exploratory Data Analysis (EDA)
- 🚗 Traffic pattern visualization
- 🤖 Machine Learning model training
- 📉 Model evaluation
- 🔮 Future traffic forecasting
- 💾 Export prediction results to CSV

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

---

## 📂 Project Structure

```text
Smart-City-Traffic-Pattern/
│
├── data/
│   ├── train_aWnotuB.csv
│   └── test_BdBKkAj.csv
│
├── output/
│   ├── forecast/
│   │   ├── future_forecast.csv
│   │   └── future_forecast.png
│   │
│   ├── graphs/
│   │   ├── all_junctions.png
│   │   ├── hourly_traffic.png
│   │   ├── junction_average.png
│   │   ├── monthly_traffic.png
│   │   ├── traffic_trend.png
│   │   ├── vehicle_distribution.png
│   │   └── weekday_traffic.png
│   │
│   └── predictions/
│       ├── actual_vs_predicted.png
│       └── model_results.csv
│
├── forecasting.py
├── main.py
├── model.py
├── preprocessing.py
├── visualization.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/PalakD42/Smart-City-Traffic-Pattern.git
```

Navigate to the project folder:

```bash
cd Smart-City-Traffic-Pattern
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 📊 Outputs

The project generates:

### 📈 Graphs

- Traffic Trend
- Hourly Traffic Analysis
- Monthly Traffic Analysis
- Weekday Traffic Analysis
- Vehicle Distribution
- Junction-wise Average Traffic
- All Junction Comparison

### 🤖 Predictions

- Actual vs Predicted Traffic Graph
- Model Performance Results (`model_results.csv`)

### 🔮 Forecast

- Future Traffic Forecast (`future_forecast.csv`)
- Future Traffic Forecast Graph

All generated files are saved in the **output/** directory.

---

## 🔄 Workflow

1. Load the traffic dataset.
2. Preprocess and clean the data.
3. Perform exploratory data analysis.
4. Visualize traffic trends.
5. Train the machine learning model.
6. Evaluate model performance.
7. Generate predictions.
8. Forecast future traffic.
9. Save graphs and results.

---

## 🚀 Future Enhancements

- Real-time traffic prediction
- LSTM-based forecasting
- Weather data integration
- Interactive dashboard using Streamlit
- API deployment with Flask/FastAPI

---

## 👩‍💻 Author

**Palak Dwivedi**

GitHub: **https://github.com/PalakD42**

---

## 📄 License

This project is developed for educational and learning purposes.

---

## ⭐ Support

If you found this project useful, don't forget to **⭐ Star** the repository!