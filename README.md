🛍️ Store Sales Forecasting Using Time Series Models
This project applies time series forecasting models to predict future sales based on historical daily data. 
It demonstrates how data-driven decision making can improve inventory planning, revenue management, and operational efficiency in the retail industry.

📂 Dataset
•	Source: Kaggle - Store Sales Forecasting by Tanaya Tipre
•	Contains daily sales records across multiple stores and items.
________________________________________
🎯 Objectives
•	Analyze and forecast monthly store sales using Prophet.
•	Evaluate trends, seasonality, and model performance (RMSE, MAPE).
•	Create a reusable Prophet model with Streamlit dashboard support.
•	Enable regional and categorical filtering in forecasts.
________________________________________
📊 Models Used
•	✅ Facebook Prophet for monthly and regional forecasting
________________________________________
📈 Key Features
•	✅ Monthly sales aggregation and trend analysis
•	✅ Model saving/loading to avoid retraining
•	✅ Evaluation metrics: RMSE and MAPE
•	✅ Future forecasting (next 6 months)
•	✅ Interactive Streamlit app with region/state/category filters
________________________________________
🔧 Tech Stack
•	Python (Pandas, Prophet, Matplotlib, Seaborn)
•	Scikit-learn for evaluation
•	Streamlit app
•	Jupyter Notebook
________________________________________
📉 Evaluation ( Results )
Metric	Monthly Forecast
RMSE	~2370.76
MAPE	~14.66%
________________________________________
📁 Project Structure
store_sales_forecasting/
├── data/
│   └── sales_data.csv
├── prophet_monthly_model.pkl
├── Store Sales Forecasting.ipynb
├── app.py (optional Streamlit app)
└── README.md
________________________________________
🚀 Future Enhancements
•	Add LSTM forecasting support
•	Improve dashboard UI in Streamlit
•	Add feature for CSV export of forecasts
•	Forecast by item or product category
