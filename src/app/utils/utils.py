import streamlit as st


# Override the default padding of streamlit app
def override_app_padding():
    st.markdown(
        """
    <style>
        .block-container {
             padding-top: 1rem;
             padding-bottom: 2rem;
             max-height: 100vh;
        }   
    </style>
    """,
        unsafe_allow_html=True,
    )


# Export all static data to be used in the app
static_data = {
    "family_options": [
        "AUTOMOTIVE",
        "BABY CARE",
        "BEAUTY",
        "BEVERAGES",
        "BOOKS",
        "BREAD/BAKERY",
        "CELEBRATION",
        "CLEANING",
        "DAIRY",
        "DELI",
        "EGGS",
        "FROZEN FOODS",
        "GROCERY I",
        "GROCERY II",
        "HARDWARE",
        "HOME AND KITCHEN I",
        "HOME AND KITCHEN II",
        "HOME APPLIANCES",
        "HOME CARE",
        "LADIESWEAR",
        "LAWN AND GARDEN",
        "LINGERIE",
        "LIQUOR,WINE,BEER",
        "MAGAZINES",
        "MEATS",
        "PERSONAL CARE",
        "PET SUPPLIES",
        "PLAYERS AND ELECTRONICS",
        "POULTRY",
        "PREPARED FOODS",
        "PRODUCE",
        "SCHOOL AND OFFICE SUPPLIES",
        "SEAFOOD",
    ],
    "day_of_week_options": {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    },
}
