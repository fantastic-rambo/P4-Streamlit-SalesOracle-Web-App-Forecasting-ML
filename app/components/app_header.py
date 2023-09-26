import streamlit as st


def app_header():
    # Split the screen into two columns with a ratio of 3:1
    header_col_1, header_col_2 = st.columns([5, 1])

    # Create the first column for the title
    with header_col_1:
        # Display a styled h1 title using Markdown
        st.markdown(
            f"<h1 style='color: #835AF1; margin-bottom: 0rem'>SalesSense</h1>",
            unsafe_allow_html=True,
        )

    # Create the second column for additional content
    with header_col_2:
        # Insert a line break to add spacing
        st.markdown("<br>", unsafe_allow_html=True)
        # Create a button labeled "View Trend" with a primary style
        view_trend_button = st.button("View Trend", type="primary")

    # Return the view trend button
    return view_trend_button
