import joblib
import pandas as pd
import numpy as np

# Load the preprocessor and the XGBoost model
preprocessor = joblib.load("/model/preprocessor.joblib")
model = joblib.load("/model/xgb_model.joblib")


# Define a function to preprocess and predict sales
def data_preprocessor(payload: dict):
    # Create a DataFrame from the payload with index 0
    payload_df = pd.DataFrame(payload, index=[0])

    # Define the minimum and maximum values for scaling
    X_min = 0.00
    X_max = 952765.716

    # Transform the input data using the preprocessor and make predictions
    scaled_value = model.predict(preprocessor.transform(payload_df))

    # Calculate the unscaled value based on the original range
    original_value = scaled_value * (X_max - X_min) + X_min

    # Round the result to 3 decimal places
    return np.round(float(original_value[0]), 3)
