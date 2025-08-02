import streamlit as st
import pandas as pd
import os
import joblib
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly
import plotly.graph_objects as go

# Title
st.title("🛍️ Store Sales Forecasting Dashboard")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("stores_sales_forecasting.csv", encoding='latin1')
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("🔎 Filter Options")
region = st.sidebar.selectbox("Select Region", df['Region'].unique())
state = st.sidebar.selectbox("Select State", df[df['Region'] == region]['State'].unique())
category = st.sidebar.selectbox("Select Category", df['Category'].unique())

# Filter dataset
filtered_df = df[(df['Region'] == region) & 
                 (df['State'] == state) & 
                 (df['Category'] == category)]

# Monthly Aggregation
monthly_sales = filtered_df.groupby(pd.Grouper(key='Order Date', freq='M'))['Sales'].sum().reset_index()
monthly_sales.columns = ['ds', 'y']

# Load or fit model
model_filename = f"prophet_{region}_{state}_{category}_monthly.pkl"
if os.path.exists(model_filename):
    model = joblib.load(model_filename)
else:
    model = Prophet()
    model.fit(monthly_sales)
    joblib.dump(model, model_filename)

# Forecast next 12 months
future = model.make_future_dataframe(periods=12, freq='M')
forecast = model.predict(future)

# Tabs
tab1, tab2 = st.tabs(["📈 Forecast", "📊 Trend & Seasonality"])

with tab1:
    st.subheader(f"📈 Forecasted Monthly Sales for {state} - {category}")
    st.plotly_chart(plot_plotly(model, forecast))
    st.caption("🧠 Forecast based on monthly aggregated sales data. Filter inputs to explore different patterns.")

with tab2:
    st.subheader("📊 Trend & Seasonality Components")
    st.plotly_chart(plot_components_plotly(model, forecast))
