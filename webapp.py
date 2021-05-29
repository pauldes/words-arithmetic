import streamlit as st
import words_arithmetic as wa

# Constants
PAGE_PREDICTIONS = "Current year predictions"
PAGE_PERFORMANCE = "Model performance analysis"
CONFIDENCE_MODE_SOFTMAX = "Softmax-based"
CONFIDENCE_MODE_SHARE = "Percentage-based"

# Page properties
st.set_page_config(
    page_title="Words arithmetic",
    page_icon=":ocean:",
    layout="centered",
    initial_sidebar_state="auto",
)

navigation_page = st.sidebar.radio("Navigate to", [PAGE_PREDICTIONS, PAGE_PERFORMANCE])
st.sidebar.markdown(
    """
**How does it work ?**

A statistical regression model is fitted on historical data (player and team stats, and MVP voting results).
It is then used to predict this season MVP based on current data.
The model predicts the *award share* (the number of points a player received for MVP award over the total points of all first-place votes).
This share can then be converted to a chance/probability using various methods (see *Predictions parameters*).
"""
)
st.sidebar.markdown(
    """
*Made by [pauldes](https://github.com/pauldes). Code on [GitHub](https://github.com/pauldes/words-arithmetic).*
"""
)

st.title("🌊 Words arithmetic")
st.markdown(
f"""
*Performing operations on word using word embeddings.*
"""
)
st.text_input('Enter some text')
st.text_area('Area for textual entry')