import streamlit as st
import words_arithmetic
from words_arithmetic import embedders

# Cached methods
@st.cache(allow_output_mutation=True)
def load_embedder(embedder_name, pretrained):
    # Mutate bar
    return embedders.GensimEmbedder(embedder_name, pretrained)

# Page properties
st.set_page_config(
    page_title="Words arithmetic",
    page_icon=":ocean:",
    layout="centered",
    initial_sidebar_state="auto",
)

#navigation_page = st.sidebar.radio("Navigate to", [PAGE_PREDICTIONS, PAGE_PERFORMANCE])
available_models = embedders.GensimEmbedder.available_models
engine = st.sidebar.selectbox('Select an engine', ["Gensim"])
model = st.sidebar.selectbox('Select a model', available_models)

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
*Performing arithmetic on words using word embeddings.*
"""
)
embedder = load_embedder("basic embedder", model)
col1, col2 = st.beta_columns([1, 3])
num_words = col1.number_input("Number of words", min_value=1, max_value=9, value=2, step=1, format="%i")
base_word = col2.text_input('Base word', 'King')
sequence = [("+", base_word)]
embedder.flush()
for i in range(num_words):
    #operand = col1.selectbox('Select', ["+", "-"])
    sequence.append(("operand-placeholder", "word-placeholder"))
    sequence[i+1] = (col1.radio(f'operand n°{i}', ["+", "-"]), col2.text_input(f'Word n°{i}'))

for (operand, word) in sequence:
    clean_word = word
    if operand == "+":
        embedder.add(clean_word)
    elif operand == "-":
        embedder.sub(clean_word)
    else:
        raise ValueError(f"Unsupported operand {operand}")

st.subheader("Results")
res = embedder.res()
first_res_word = res[0][0]
st.text("".join(f"{operand} {word} " if i>0 else f"{word} " for i,  (operand, word) in enumerate(sequence)) + f"= {first_res_word}")
st.info("\n\n".join(f"{w} ({s:.2f})" for w,s in embedder.res()))