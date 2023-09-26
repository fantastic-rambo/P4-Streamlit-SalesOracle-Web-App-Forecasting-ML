import streamlit as st
from datetime import date


# Render a predicted sale with custom styling
def render_predicted_sale(forecast_date=date.today(), forecast_sale=12):
    # Check and apply the appropriate color formatting
    color = "#FF6B57" if forecast_sale < 0 else "#4CAF50"

    # Use st.markdown to display the content with HTML styling
    return st.markdown(
        f"""<div style='background-color: {color}; padding: .5rem 1rem; border-radius: .5rem; color: white; margin-bottom: .5rem; display: flex; align-items: center; justify-content: center; flex-direction: column'>
                    <p style='margin-bottom: .1rem'>Date: {forecast_date} </p>
                    <h1 style='margin-bottom: -.6rem; margin-top: -.6rem; color: white'>Sale: ${forecast_sale}</h1>
                </div>
            """,
        unsafe_allow_html=True,
    )
