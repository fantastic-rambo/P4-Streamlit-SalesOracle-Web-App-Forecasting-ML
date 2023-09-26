import streamlit as st
import pandas as pd
import numpy as np
import joblib

#columns=[date, sales, onpromotion, dayofweek, lag_1, rolling_mean, family]

# Load the sales prediction model 
model = joblib.load("C:/Users/IKE/OneDrive - Azubi Africa/Project1/P4-Streamlit-SalesOracle-Web-App-Forecasting-ML/model/xgb_model.joblib")

# Load the preprocessor steps using Joblib
preprocessor = joblib.load(r"C:\Users\IKE\OneDrive - Azubi Africa\Project1\P4-Streamlit-SalesOracle-Web-App-Forecasting-ML\model\preprocessor.joblib")

# Create a Streamlit app title
st.title("Sales Prediction App")

# Add a brief description
st.write("This app predicts sales based on input features: Date, Family, Sales, On Promotion, Day of the Week, Lag_1, and Rolling Mean.")

# Sidebar for user input
st.sidebar.header("Input Parameters")

# Input elements for user interaction
date = st.sidebar.date_input("Select Date")
family = st.sidebar.selectbox("Select Family", ['AUTOMOTIVE', 'BABY CARE', 'BEAUTY', 'BEVERAGES', 'BOOKS', 'BREAD/BAKERY',
 'CELEBRATION', 'CLEANING', 'DAIRY', 'DELI', 'EGGS', 'FROZEN FOODS', 'GROCERY I',
 'GROCERY II', 'HARDWARE', 'HOME AND KITCHEN I', 'HOME AND KITCHEN II',
 'HOME APPLIANCES', 'HOME CARE', 'LADIESWEAR', 'LAWN AND GARDEN', 'LINGERIE',
 'LIQUOR,WINE,BEER', 'MAGAZINES', 'MEATS', 'PERSONAL CARE', 'PET SUPPLIES',
 'PLAYERS AND ELECTRONICS', 'POULTRY', 'PREPARED FOODS', 'PRODUCE',
 'SCHOOL AND OFFICE SUPPLIES', 'SEAFOOD'])

sales = st.sidebar.number_input("Enter Sales")
onpromotion = st.sidebar.checkbox("On Promotion")
day_of_week = st.sidebar.selectbox("Select Day of the Week", [1,2,3,4,5,6,7])
lag_1 = st.sidebar.number_input("Enter Lag_1")
rolling_mean = st.sidebar.number_input("Enter Rolling Mean")

# Create a dictionary with user input data
user_input_data = {
    "Date": date,
    "Family": family,
    "Sales": sales,
    "On Promotion": onpromotion,
    "Day of the Week": day_of_week,
    "Lag_1": lag_1,
    "Rolling Mean": rolling_mean
}

# Add a "Predict" button
predict_button = st.sidebar.button("Predict")

if predict_button:
    # Convert the user input data into a DataFrame
    user_input_df = pd.DataFrame([user_input_data])

    # Perform predictions using the loaded model
    try:
        predicted_sales = model.predict(user_input_df)
        st.write(f"Predicted Sales: ${predicted_sales[0]:.2f}")
    except Exception as e:
        st.error(f"An error occurred during prediction: {str(e)}")
    else:
        st.success("Prediction successful!")

