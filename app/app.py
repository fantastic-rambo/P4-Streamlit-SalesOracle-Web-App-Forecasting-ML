import streamlit as st
import pandas as pd

# Import custom functions and components
from utils.utils import override_app_padding
from components.app_header import app_header
from components.new_pred_form import new_pred_form
from components.sidebar import sidebar

# Set page title and layout
st.set_page_config(page_title="SalesSense Prediction", layout="wide")

# Apply the function to override default padding
override_app_padding()

# Define custom color palette
custom_color_palette = ["#835AF1", "#37AA9C", "#B8F7D4", "#94F3E4"]

# Check if 'prediction_df' exists in session state; if not, create an empty DataFrame
if "prediction_df" not in st.session_state:
    st.session_state.prediction_df = pd.DataFrame(columns=["Date", "Sale"])

# Implement the app header and get the 'view_trend_button' status
view_trend_button = app_header()

# Implement the sidebar
sidebar()

# Check the 'view_trend_button' status to decide what to display
if view_trend_button is False:
    # Implement the prediction form
    new_pred_form()
else:
    # Define a function that sets 'view_trend_button' to False
    def callback_func():
        view_trend_button = False

    # Display sales trend chart
    st.subheader("Sales Trend")
    st.line_chart(st.session_state["prediction_df"], x="Date", y="Sale")

    # Add a button to reset 'view_trend_button' to False
    st.button(
        "Make Prediction",
        on_click=lambda: callback_func(),
        use_container_width=True,
    )
