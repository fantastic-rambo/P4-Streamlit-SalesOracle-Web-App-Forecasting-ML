import streamlit as st
import pandas as pd

# from utils.utils import data_preprocessor
from utils.data_preprocessor import data_preprocessor
from utils.utils import static_data
from components.render_predicted_sale import render_predicted_sale


def new_pred_form():
    # Display a subheader for making a new prediction
    st.subheader("New Prediction")

    # Create a container to organize the form elements
    with st.container():
        # Create a form for user input
        with st.form(key="sales_prediction_form", clear_on_submit=True):
            # Split the form into two columns
            form_col_1, form_col_2 = st.columns(2)

            # Form column 1
            with form_col_1:
                # Create a dropdown for selecting the family of the store
                family = st.selectbox(
                    label="Please Select the Family of the Store",
                    options=static_data["family_options"],
                    help="Select the family of the store",
                )

                # Create a dropdown for selecting the day of the week
                day_of_week = st.selectbox(
                    label="Select day of the week",
                    options=list(static_data["day_of_week_options"].keys()),
                    format_func=lambda x: static_data["day_of_week_options"][
                        list(static_data["day_of_week_options"].keys()).index(x) + 1
                    ],
                    help="Select the forecast day",
                )

                # Create a date input field for choosing the forecast date
                current_date = st.date_input(
                    label="Choose the forecast date", help="Choose the forecast date"
                )

            # Form column 2
            with form_col_2:
                # Create a numeric input field for the number of items on promotion
                onpromotion = st.number_input(
                    label="Enter the number of items on promotion",
                    min_value=0,
                    help="Enter the number of items on promotion",
                )

                # Create a numeric input field for entering previous sales
                lag_1 = st.number_input(
                    label="Enter previous sales",
                    help="Enter the previous sales value or 0",
                )

                # Create a numeric input field for entering rolling mean
                rolling_mean = st.number_input(
                    label="Enter rolling mean",
                    min_value=0,
                    help="Enter the rolling mean value or 0",
                )

            # Create a form submit button with a primary style
            is_form_submitted = st.form_submit_button(
                label="Submit",
                use_container_width=True,
                type="primary",
            )

            # Create payload to send the data
            payload = {
                "date": current_date,
                "family": family,
                "onpromotion": onpromotion,
                "day_of_week": day_of_week,
                "lag_1": lag_1,
                "rolling_mean": rolling_mean,
            }

            if is_form_submitted:
                # Calculate the sale
                forecast_sale = data_preprocessor(payload=payload)

                # Create a new DataFrame with the prediction data
                new_row = pd.DataFrame(
                    {"Date": [current_date], "Sale": [forecast_sale]}
                )

                # Update the prediction df and add a new prediction
                st.session_state.prediction_df = pd.concat(
                    [st.session_state.prediction_df, new_row], ignore_index=True
                )

                # Display the Prediction
                render_predicted_sale(
                    forecast_date=current_date,
                    forecast_sale=forecast_sale,
                )
