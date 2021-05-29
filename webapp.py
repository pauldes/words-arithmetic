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

###
###
###
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
word = st.text_input('Base word')