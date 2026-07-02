import pandas as pd
import streamlit as st
from prophet import Prophet
import plotly.express as px

# -----------------------------
# DASHBOARD TITLE
# -----------------------------
st.title("Demand Prediction & Demand Distribution Dashboard")

# -----------------------------
# LOAD DATASET
# -----------------------------
df = pd.read_csv("retail_sales_dataset.csv")

# -----------------------------
# SHOW DATASET
# -----------------------------
st.subheader("Dataset Preview")
st.write(df.head())

# -----------------------------
# CONVERT DATE COLUMN
# -----------------------------
df['Date'] = pd.to_datetime(df['Date'])

# -----------------------------
# DEMAND PREDICTION SECTION
# -----------------------------
st.header("Demand Prediction")

# Group sales by date
sales_data = df.groupby('Date')['Total Amount'].sum().reset_index()

# Rename columns for Prophet
sales_data = sales_data.rename(columns={
    'Date': 'ds',
    'Total Amount': 'y'
})

# Train Prophet Model
model = Prophet()

model.fit(sales_data)

# Create Future Dates
future = model.make_future_dataframe(periods=30)

# Predict Future Demand
forecast = model.predict(future)

# Show Prediction Table
st.subheader("Future Predictions")
st.write(forecast[['ds', 'yhat']].tail())

# Prediction Graph
fig1 = px.line(
    forecast,
    x='ds',
    y='yhat',
    title='Future Demand Prediction'
)

st.plotly_chart(fig1)

# -----------------------------
# DEMAND DISTRIBUTION SECTION
# -----------------------------
st.header("Demand Distribution")

# -----------------------------
# CATEGORY-WISE DEMAND
# -----------------------------
st.subheader("Demand by Product Category")

category_sales = df.groupby('Product Category')['Total Amount'].sum().reset_index()

fig2 = px.bar(
    category_sales,
    x='Product Category',
    y='Total Amount',
    title='Product Category Demand Distribution'
)

st.plotly_chart(fig2)

# -----------------------------
# GENDER-WISE DEMAND
# -----------------------------
st.subheader("Demand Distribution by Gender")

gender_sales = df.groupby('Gender')['Total Amount'].sum().reset_index()

fig3 = px.pie(
    gender_sales,
    names='Gender',
    values='Total Amount',
    title='Gender-wise Demand Distribution'
)

st.plotly_chart(fig3)

# -----------------------------
# AGE-WISE DEMAND
# -----------------------------
st.subheader("Demand Distribution by Age")

fig4 = px.histogram(
    df,
    x='Age',
    y='Total Amount',
    title='Age-wise Demand Distribution'
)

st.plotly_chart(fig4)

# -----------------------------
# MONTHLY SALES DISTRIBUTION
# -----------------------------
st.subheader("Monthly Demand Distribution")

# Extract month
df['Month'] = df['Date'].dt.month

monthly_sales = df.groupby('Month')['Total Amount'].sum().reset_index()

fig5 = px.line(
    monthly_sales,
    x='Month',
    y='Total Amount',
    title='Monthly Demand Distribution'
)

st.plotly_chart(fig5)

# -----------------------------
# SUCCESS MESSAGE
# -----------------------------
st.success("Demand Prediction and Demand Distribution Completed Successfully")
