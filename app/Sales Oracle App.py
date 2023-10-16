# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Create a Streamlit app title
st.title("Welcome to the SalesOracle App")

# Add a brief description
st.write("This app demonstrates a simple Sales Forecasting model.")

# Sidebar for user input
st.sidebar.header("Input Parameters")

# Input elements for user interaction
input_feature = st.sidebar.text_input("Enter a feature value:")
input_feature = float(input_feature) if input_feature else None

# Load or create a dataset (in this example, we'll use a simple example dataset)
data = pd.DataFrame({
    "X": np.arange(1, 11),
    "Y": [2.1, 3.9, 5.8, 8.1, 9.7, 12.1, 14.2, 16.8, 18.5, 21.3]
})

# Display the dataset
st.write("Sample Dataset:")
st.write(data)

# Train a simple linear regression model
X = data[['X']]
y = data['Y']

model = LinearRegression()
model.fit(X, y)

# Make predictions using the input feature (if provided)
if input_feature is not None:
    predicted_value = model.predict([[input_feature]])
    st.write(f"Predicted Y value for X={input_feature}: {predicted_value[0]:.2f}")

# Evaluate the model
y_pred = model.predict(X)
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

st.write(f"Mean Squared Error: {mse:.2f}")
st.write(f"R-squared: {r2:.2f}")

# Plot the dataset and regression line
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
plt.scatter(X, y, label="Actual")
plt.plot(X, y_pred, color='red', linewidth=2, label="Regression Line")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
st.pyplot(plt)

# Add a link to the source code on GitHub (optional)
st.sidebar.markdown("[Source Code on GitHub](https://github.com/your-username/your-repo)")

