# Demand Prediction and Distribution Dashboard Using Time Series Forecasting

## Abstract

The Demand Prediction and Distribution Dashboard is a Time Series Forecasting application developed to predict future product demand using historical sales data. The system analyzes past demand trends and generates future demand forecasts using the **Prophet** forecasting model. An interactive dashboard built with **Streamlit** provides users with visual insights into demand trends, future forecasts, and demand distribution. This project demonstrates the application of time series forecasting in inventory management and supply chain planning to reduce stock shortages, minimize overstocking, and improve business decision-making.

---

# Introduction

Accurate demand forecasting is one of the most important aspects of inventory management and supply chain optimization. Organizations often struggle with either excess inventory or stock shortages due to inaccurate demand estimation.

Time Series Forecasting uses historical sales information to identify trends, seasonality, and future demand patterns. This project presents an AI-powered dashboard capable of forecasting future product demand and visualizing demand distribution. The dashboard enables businesses to make informed inventory decisions and improve operational efficiency.

---

# Literature Review

Demand forecasting has been extensively studied in retail, manufacturing, and supply chain management. Traditional forecasting methods relied on moving averages and statistical models such as ARIMA. While these methods perform well on simple datasets, they often struggle with seasonal patterns and complex trends.

Modern forecasting techniques such as Facebook Prophet, Long Short-Term Memory (LSTM) Networks, and Gradient Boosting algorithms provide more accurate predictions by learning historical demand behavior.

Facebook Prophet has gained popularity because of its simplicity, accuracy, and ability to model trend, seasonality, and holiday effects with minimal preprocessing. This project utilizes Prophet due to its effectiveness in business forecasting applications.

---

# Methodology

The project follows a standard Time Series Forecasting workflow.

## Step 1: Data Collection

Historical sales data is collected in CSV format containing:

- Date
- Sales/Demand

## Step 2: Data Preprocessing

- Import dataset using Pandas
- Check for missing values
- Rename columns to Prophet format
  - Date → ds
  - Sales → y

## Step 3: Model Training

The Prophet forecasting model is trained using historical demand data.

## Step 4: Future Forecasting

The trained model predicts future demand for the next predefined period (e.g., 30 days).

## Step 5: Dashboard Development

A Streamlit dashboard displays:

- Historical demand
- Forecasted demand
- Demand trend graph
- Demand distribution chart

---

# Implementation

## Programming Language

- Python

## Development Environment

- Visual Studio Code (VS Code)

## Libraries Used

- Pandas
- NumPy
- Streamlit
- Prophet
- Plotly
- Matplotlib

## Machine Learning Model

- Prophet Time Series Forecasting Model

## Dataset

- Historical Sales Dataset (CSV)

## Implementation Steps

1. Load historical sales dataset.
2. Preprocess the data.
3. Train Prophet forecasting model.
4. Generate future demand predictions.
5. Visualize forecast using interactive charts.
6. Display demand distribution dashboard.

---

# Results

The developed system successfully forecasts future product demand using historical sales records.

The Streamlit dashboard provides:

- Historical demand visualization
- Future demand prediction
- Interactive demand trend graph
- Demand distribution analysis

The forecasting model enables users to estimate future inventory requirements accurately.

---

# Conclusion

The Demand Prediction and Distribution Dashboard demonstrates the practical application of Time Series Forecasting in inventory and supply chain management. Using historical sales data, the Prophet forecasting model predicts future demand with high efficiency. The interactive dashboard provides valuable insights into demand trends and supports data-driven inventory planning, helping businesses reduce operational costs and improve customer satisfaction.

---

# Future Scope

The project can be enhanced by incorporating:

- Multiple product demand forecasting
- Regional demand analysis
- Weather-based demand prediction
- Festival and holiday demand forecasting
- Integration with ERP systems
- Real-time sales database
- Deep Learning (LSTM) forecasting
- Cloud deployment
- Automated inventory recommendations
- PDF and Excel report generation
- Mobile dashboard application

---

# Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Prophet
- Plotly
- Matplotlib
- Visual Studio Code
- CSV Dataset

---

# Project Structure

```
Demand_Prediction_Project/
│
├── app.py
├── model.py
├── sales.csv
├── requirements.txt
├── README.md
├── .gitignore
│
├── models/
│   └── forecast_model.pkl
│
├── assets/
│   ├── dashboard.png
│   └── forecast.png
│
├── notebooks/
│   └── Demand_Analysis.ipynb
│
└── venv/
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/your-username/demand-prediction-dashboard.git
```

Move into project directory

```bash
cd demand-prediction-dashboard
```

Install dependencies

```bash
pip install pandas numpy prophet streamlit plotly matplotlib
```

or

```bash
pip install -r requirements.txt
```

---

# Running the Project

Run the application

```bash
python -m streamlit run app.py
```

The dashboard will open automatically in your browser.

---

# Features

- Historical Demand Visualization
- Future Demand Forecasting
- Interactive Dashboard
- Time Series Forecasting
- Demand Distribution Analysis
- Real-Time Prediction
- CSV Dataset Support
- Interactive Charts
- User-Friendly Interface

---

# Output

### Input

- Historical Sales Dataset

### Output

- Future Demand Prediction
- Demand Trend Graph
- Demand Distribution Dashboard
- Forecast Table

---

# References

1. Taylor, S. J., & Letham, B., "Forecasting at Scale," *The American Statistician*, Vol. 72, No. 1, pp. 37–45, 2018.
2. Prophet Documentation.
3. Streamlit Documentation.
4. Pandas Documentation.
5. Plotly Documentation.
6. Hyndman, R. J., & Athanasopoulos, G., *Forecasting: Principles and Practice*, OTexts, 2021.
7. Bishop, C. M., *Pattern Recognition and Machine Learning*, Springer, 2006.

---



