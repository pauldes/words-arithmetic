import streamlit as st
import words_arithmetic.embedder

# Constants
PAGE_PREDICTIONS = "Current year predictions"
PAGE_PERFORMANCE = "Model performance analysis"
CONFIDENCE_MODE_SOFTMAX = "Softmax-based"
CONFIDENCE_MODE_SHARE = "Percentage-based"
NUM_WORDS = 3

embedder = words_arithmetic.embedder.Embedder("basic embedder")

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
base_word = st.text_input('Base word')
#hit = st.button('Hit me')
sequence = []
col1, col2 = st.beta_columns([1, 3])
for i in range(NUM_WORDS):
    #operator = col1.selectbox('Select', ["+", "-"])
    sequence.append(("operator-placeholder", "word-placeholder"))
    sequence[i] = (col1.radio(f'Operator n°{i}', ["+", "-"]), col2.text_input(f'Word n°{i}'))

for (operator, word) in sequence:
    st.write(f"and {operator} the word {word}")