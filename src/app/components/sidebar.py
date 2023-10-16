import streamlit as st

# Import the component to render predicted sales and some static data
from components.render_predicted_sale import render_predicted_sale
from utils.utils import static_data


# Define the sidebar component
def sidebar():
    # In the Streamlit sidebar
    with st.sidebar:
        # Expandable section for Store Family
        with st.expander("STORE FAMILY"):
            # Iterate over family options and display them with custom styling
            for family in static_data["family_options"]:
                st.markdown(
                    f"""
                    <div style='background-color: #835AF1; padding: .5rem 1rem; border-radius: .5rem; color: white; margin-bottom: .5rem'>{family}</div>
                    """,
                    unsafe_allow_html=True,
                )

        # Expandable section for Sales Predictions
        with st.expander("SALES PREDICTIONS"):
            # Render predicted sale for each of the predictions
            for _, row in st.session_state["prediction_df"].iterrows():
                render_predicted_sale(
                    forecast_date=row["Date"], forecast_sale=row["Sale"]
                )  # Use a component to render predictions

        # Add an empty Markdown element to create space
        st.markdown(f"{'<br>'*2}", unsafe_allow_html=True)

        # Expandable section for About App
        with st.expander("ABOUT APP"):
            # Provide information about the SalesSense app
            st.write(
                "SalesSense is an intuitive web app powered by cutting-edge machine learning models that provides real-time sales forecasts, helping businesses optimize inventory, boost profits, and make data-driven decisions effortlessly"
            )
