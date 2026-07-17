# 🚦 Smart City Traffic Pattern Prediction

A Machine Learning project that analyzes historical traffic data, visualizes traffic patterns, and predicts future traffic flow for smart city traffic management.

---

## 📌 Features

- 📊 Data preprocessing and cleaning
- 📈 Exploratory Data Analysis (EDA)
- 🚗 Traffic trend visualization
- 🤖 Machine Learning-based traffic prediction
- 🔮 Future traffic forecasting
- 📉 Automatic graph generation
- 💾 Export prediction results to CSV

---

## 🛠️ Tech Stack

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
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
├── preprocessing.py
├── model.py
├── visualization.py
├── forecasting.py
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
└── __pycache__/ (ignored)
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/PalakD42/Smart-City-Traffic-Pattern.git
```

### Navigate to the project directory

```bash
cd Smart-City-Traffic-Pattern
```

### Install the required dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

Execute:

```bash
python main.py
```

---

## 📊 Outputs

After running the project, the following outputs are generated automatically.

### 📈 Graphs

- Traffic Trend Analysis
- Hourly Traffic Distribution
- Monthly Traffic Analysis
- Weekday Traffic Analysis
- Vehicle Distribution
- Junction-wise Average Traffic
- All Junction Comparison

### 🤖 Prediction

- Actual vs Predicted Traffic Graph
- Model Performance Results (CSV)

### 🔮 Forecast

- Future Traffic Forecast (CSV)
- Future Traffic Forecast Graph

All outputs are stored inside the **output/** folder.

---

## 🔄 Project Workflow

1. Load the traffic dataset.
2. Preprocess and clean the data.
3. Perform exploratory data analysis.
4. Visualize traffic patterns.
5. Train the machine learning model.
6. Evaluate model performance.
7. Predict traffic volume.
8. Forecast future traffic.
9. Save graphs and prediction results.

---

## 📁 Dataset

The project uses historical traffic data containing:

- Date
- Time
- Junction ID
- Vehicle Count

---

## 📄 .gitignore

The project includes a `.gitignore` file to exclude unnecessary files from version control.

```gitignore
# Python cache
__pycache__/
*.py[cod]

# Virtual environments
venv/
.venv/
env/

# IDE settings
.vscode/
.idea/

# Environment variables
.env

# Build files
build/
dist/
*.egg-info/

# Log files
*.log

# Operating system files
.DS_Store
Thumbs.db

# Generated outputs
output/
```

---

## 🚀 Future Enhancements

- Deep Learning (LSTM) traffic forecasting
- Real-time traffic prediction
- Weather data integration
- Interactive Streamlit dashboard
- Traffic congestion alerts
- Web deployment using Flask/FastAPI

---

## 👨‍💻 Author

**Palak Dwivedi**

GitHub: **https://github.com/PalakD42**

---

## 📄 License

This project is developed for educational and academic purposes.

---

## ⭐ Show Your Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub.